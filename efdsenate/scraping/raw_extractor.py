import re
from urllib.parse import urljoin

from constants import hparse

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

