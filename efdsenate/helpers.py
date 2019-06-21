from lxml.html import fromstring
import re

def cleantext(txt):
    return re.sub(r'\s+', ' ', txt).strip()

def hparse(html):
    return fromstring(html)
