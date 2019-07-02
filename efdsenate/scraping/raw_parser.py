from datetime import datetime
import re

from helpers import cleantext
from scraping.raw_extractor import _extract_doc_title, _extract_doc_url
from scraping.raw_extractor import _extract_doc_id, _extract_related_date


PARSED_HEADERS  = {
    'state': str,  # state can only be determined from the filename, not the data
    'date': lambda r: datetime.strptime(r[4], '%m/%d/%Y').strftime('%Y-%m-%d'),
    'last_name': lambda r: r[1].upper(),
    'first_name': lambda r: r[0].upper(),
    'filer_type': lambda r: r[2],
    'doc_type': lambda r: _extract_doc_title(r[3]),    # e.g. Finance Report
    'doc_subtype':  str,  # e.g. Annual, New Filer, Candidate, Termination
    'doc_filetype':  str, # e.g. paper/html
    'amendment_number':  str,
    'doc_related_date': str,
    'extension_number':  str,
    'doc_title': lambda r: _extract_doc_title(r[3]),
    'doc_id': lambda r: _extract_doc_id(r[3]),
    'doc_url': lambda r: _extract_doc_url(r[3]),
}

FDREPORT_SUBTYPES= {
    'annual': 'Annual Report',
    'termination': 'Termination Report',
    'new filer': 'New Filer Report',
    'candidate': 'Candidate Report',
}


def classify_doc_meta(title, url):
    title = cleantext(title)
    d = {'doc_type': None,
         'doc_subtype': None,
         'amendment_number': None,
         'extension_number': None,
         'doc_filetype': None, }

    # first, the doc_filetype
    if '/view/paper' in url:
        d['doc_filetype'] = 'paper'
    else:
        d['doc_filetype'] = 'html'

    #######################################
    # now, check if it's an amendment
    if 'Amendment' in title:
        # extract an amendment number
        _ax = re.search(r'Amendment *(\d+)', title)
        d['amendment_number'] = int(_ax.groups()[0]) if _ax else 1


    # only fdreports and extensions have subtypes
    d['doc_type'] = _classify_doc_type(title, url)

    if d['doc_type'] in ['Financial Disclosure Report', 'Extension Notice']:
        d['doc_subtype'] = _subclassify_fdreport(title)

    if d['doc_type'] == 'Extension Notice':
        # extract the extension number
        _ex = re.search(r'Extension *(\d+)', title)
        # presumably non-marked extensions are the first of their kind
        d['extension_number'] = int(_ex.groups()[0]) if _ex else 1



    d['doc_related_date'] = _extract_related_date(title)

    return d


def _classify_doc_type(title, url):
   ###########################################
    # Now for the doctypes; start with the easy ones
    dt = ''
    if 'Miscellaneous' in title:
        dt = 'Miscellaneous Information'
    elif 'Blind Trust' in title:
        dt = 'Blind Trust'
    elif 'extension-notice' in url or 'Extension' in title:
        dt = 'Extension Notice'
    elif any(k in title.lower() for k in FDREPORT_SUBTYPES.keys()):
        dt = 'Financial Disclosure Report'
    elif 'Periodic Transaction Report' in title:
        dt = 'Periodic Transaction Report'
    else:
        raise ValueError("`{}` did not match an expected doc_type".format(title))

    return dt

def _subclassify_fdreport(title):
    """
    presumably, `title` belongs to a document that is already
    known to have a doc_type of Financial Disclosure Report
    """
    t = title.lower()
    x = next((v for k, v in FDREPORT_SUBTYPES.items() if k in t), None)
    if x:
        return x
    else:
        if re.match(r'^report due date', t): # weird edge case
            return 'Annual Report'
        else:
            raise ValueError("Could not classify the subtype for title: {}".format(title))





def parse_single_raw_record(record):
    d = {k: cleantext(foo(record)) for k, foo in PARSED_HEADERS.items()}
    d.update(classify_doc_meta(d['doc_title'], d['doc_url']))
    for k, v in d.items():
        d[k] = str(v) if v else ''
    return d

def parse_raw_records(records):
    return [parse_single_raw_record(r) for r in records]



if __name__ == '__main__':
    print('foo')
