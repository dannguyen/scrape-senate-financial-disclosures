"""
fdr is short for Financial Disclosure Report
"""
from lxml import etree
from pathlib import Path

from helpers import cleantext
from formparse.fdrform.utils import extract_sections, parse_section

# from formparse.fdrform.sec01 import parsec_01
# from formparse.fdrform.sec02 import parsec_02
# from formparse.fdrform.sec03 import parsec_03
# from formparse.fdrform.sec04a import parsec_04a
# from formparse.fdrform.sec04b import parsec_04b
# from formparse.fdrform.sec05 import parsec_05
# from formparse.fdrform.sec06 import parsec_06
# from formparse.fdrform.sec07 import parsec_07
# from formparse.fdrform.sec08 import parsec_08
# from formparse.fdrform.sec09 import parsec_09
# from formparse.fdrform.sec10 import parsec_10


def main():
    d = {}
    SRC_FNAME = Path('archive', 'samples', 'webpages', '2015-annual-report-corker.html')
    html = SRC_FNAME.read_text()
    sections = extract_sections(html)

    d['parts'] = []

    d['parts'].append(parse_section(sections[0]))
    d['parts'].append(parse_section(sections[1]))
    d['parts'].append(parse_section(sections[2]))
    d['parts'].append(parse_section(sections[3]))
    d['parts'].append(parse_section(sections[4]))
    d['parts'].append(parse_section(sections[5]))
    d['parts'].append(parse_section(sections[6]))
    d['parts'].append(parse_section(sections[7]))
    d['parts'].append(parse_section(sections[8]))
    d['parts'].append(parse_section(sections[9]))
    d['parts'].append(parse_section(sections[10]))

    return d


if __name__ == '__main__':
    print('run formparser.py')
