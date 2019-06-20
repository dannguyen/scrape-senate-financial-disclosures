
  # [
  #   "Thomas H",
  #   "Tuberville",
  #   "Candidate",
  #   "<a href=\"/search/view/extension-notice/regular/f18c040a-bc87-453c-af9e-38c634f0d8ff/\" target=\"_blank\">Candidate Report  Due Date Extension 1</a>",
  #   "05/14/2019"
  # ],
  # [
  #   "Doug",
  #   "Jones",
  #   "Senator",
  #   "<a href=\"/search/view/extension-notice/regular/3e2737e6-f4d4-4315-9301-14caa4518872/\" target=\"_blank\">Annual Report for 2018 Due Date Extension 1</a>",
  #   "05/13/2019"
  # ],

from datetime import datetime
from lxml.html import fromstring as hparse
from urllib.parse import urljoin
import re

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


# Sample URLS:

# https://efdsearch.senate.gov/search/view/ptr/265964e0-3d22-4a52-af4f-37916b56390d/
# https://efdsearch.senate.gov/search/view/annual/cc198326-0f50-4f47-8b03-a5c6440f400f/
# https://efdsearch.senate.gov/search/view/extension-notice/regular/728ce459-7df0-4e94-b841-f00d07197a9e/


def classify_doc_meta(title, url):
    title = _cleantext(title)
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


# def _classify_html_file(metadata, title, url):
#     d = metadata.copy()

#     viewtype = re.search(r'/view/([^/]+)', url).groups()[0]
#     if viewtype == 'extension-notice':
#         d['doc_type'] = 'Extension'
#         # extract the extension number
#         _ex = re.search(r'Extension *(\d+)')
#         # presumably non-marked extensions are the first of their kind
#         d['extension_number'] = _ex.groups()[0] if _ex else 1
#         # seems like all of the extensions have to do with the financial reports
#         d['doc_subtype'] = _subclassify_fd_report(d['doc_title'])


# def _classify_paper_file(metadata, title, url):
#     d = metadata.copy()

#     return d

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

def _extract_related_date(title):
    # if there's a full date , we go for that first
    dx = re.search(r'(\d{2})/(\d{2})/(\d{4})', title)
    if dx:
        m, d, y = dx.groups()
        return '{}-{}-{}'.format(y, m, d)

    yx = re.search(r'20\d\d', title)
    if yx:
        return yx.group()
    else:
        return None

def _subclassify_fdreport(title):
    """
    presumably, `title` belongs to a document that is already
    known to have a doc_type of Financial Disclosure Report
    """
    t = _cleantext(title.lower())
    x = next((v for k, v in FDREPORT_SUBTYPES.items() if k in t), None)
    if x:
        return x
    else:
        if re.match(r'^report due date', t): # weird edge case
            return 'Annual Report'
        else:
            raise ValueError("Could not classify the subtype for title: {}".format(title))

    # if 'annual' in t:
    #     x = 'Annual Report'
    # elif 'candidate' in t:
    #     x = 'Candidate Report'
    # elif 'new filer' in t:
    #     x = 'New Filer Report'
    # elif 'terminat' in t:
    #     x = 'Termination Report'
    # else:
    #     raise ValueError("`{}` did not match an expected report subtype".format(title))
    # return x

def _extract_doc_id(htmlstr):
    href = hparse(htmlstr).cssselect('a')[0].attrib['href']
    x = re.search(r'/([^/]+)//?$', href) # for now, we track the IDs of URLs that end with double slashes...
    if x:
        return x.groups()[0]
    else:
        return ''

def _extract_doc_url(htmlstr):
    href = hparse(htmlstr).cssselect('a')[0].attrib['href']
    return urljoin('https://efdsearch.senate.gov', href)

def _extract_doc_title(htmlstr):
    return hparse(htmlstr).cssselect('a')[0].text

def _cleantext(txt):
    return re.sub(r'\s+', ' ', txt).strip()

#################################




def parse_single_raw_record(record):
    d = {k: _cleantext(foo(record)) for k, foo in PARSED_HEADERS.items()}
    d.update(classify_doc_meta(d['doc_title'], d['doc_url']))
    for k, v in d.items():
        d[k] = str(v) if v else ''
    return d

def parse_raw_records(records):
    return [parse_single_raw_record(r) for r in records]
