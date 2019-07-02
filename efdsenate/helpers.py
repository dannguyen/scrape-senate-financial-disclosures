from lxml.html import fromstring
import re

def cleantext(txt):
    return re.sub(r'\s+', ' ', txt).strip() if txt else ''

def hparse(html):
    return fromstring(html)

def slugify(txt):
    return re.sub(r'\s', '_', cleantext(txt).lower())
