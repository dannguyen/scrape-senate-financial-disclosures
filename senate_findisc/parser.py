
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
    # 'doc_subtype':  str,  # e.g. Annual, New Filer, Candidate, Termination
    # 'amendment_num':  str,
    # 'doc_filetype':  str, # e.g. paper/html
    'doc_title': lambda r: _extract_doc_title(r[3]),
    'doc_url': lambda r: _extract_doc_url(r[3]),
    'doc_id': lambda r: _extract_doc_id(r[3]),


}




def _classify_doc_type(htmlstr):
    url = _extract_doc_url(htmlstr)
    doctitle = _extract_doc_title(htmlstr)

    """
    doctypes = [
        'Annual Report',
            'New Filer',
            'Termination'
            'Candidate'

        'Blind Trust',
        'Miscellaneous Information',
    ]
    """

    return txt

def _extract_doc_id(htmlstr):
    href = hparse(htmlstr).cssselect('a')[0].attrib['href']
    x = re.search(r'/([^/]+)/$', href)
    if x:
        return x.groups()[0]
    else:
        return ''

def _extract_doc_url(htmlstr):
    href = hparse(htmlstr).cssselect('a')[0].attrib['href']
    return urljoin('https://efdsearch.senate.gov', href)

def _extract_doc_title(htmlstr):
    return hparse(htmlstr).cssselect('a')[0].text

def parse_single_raw_record(record):
    d = {k: foo(record).strip() for k, foo in PARSED_HEADERS.items()}
    return d

def parse_raw_records(records):
    return [parse_single_raw_record(r) for r in records]
