from efdsenate.scraping.raw_parser import classify_doc_meta
import pytest


def test_classify_doc_meta_basic_html():
    meta = classify_doc_meta('Annual Report', 'http://example.com/something/view/annual/sadfklj')
    assert type(meta) == dict
    assert meta['doc_type'] == 'Financial Disclosure Report'
    assert meta['doc_subtype'] == 'Annual Report'
    assert meta['doc_filetype'] == 'html'
    assert meta['amendment_number'] is None
    assert meta['extension_number'] is None
    assert meta['doc_related_date'] is None



def test_classify_doc_meta_basic_paper():
    t = 'Periodic Transaction Report for 02/08/2019'
    u = 'https://efdsearch.senate.gov/search/view/paper/d26e9de9-163b-451f-ae32-fab6e211e5d0/'

    meta = classify_doc_meta(t, u)
    assert meta['doc_type'] == 'Periodic Transaction Report'
    assert meta['doc_subtype'] == None
    assert meta['doc_filetype'] == 'paper'
    assert meta['amendment_number'] is None
    assert meta['extension_number'] is None
    assert meta['doc_related_date'] == '2019-02-08'




def test_classify_doc_meta_extension_notices():
    t = 'Termination Report in 2017 Due Date Extension 3'
    u = 'example.com'

    meta = classify_doc_meta(t, u)
    assert meta['doc_type'] == 'Extension Notice'
    assert meta['doc_subtype'] == 'Termination Report'
    assert meta['doc_filetype'] == 'html'
    assert meta['amendment_number'] is None
    assert meta['extension_number'] is 3
    assert meta['doc_related_date'] == '2017'


def test_classify_doc_meta_amended_extension_notices():
    t = 'Annual Report for 2015 Due Date Extension 2 (Amendment 1)'
    u = 'https://efdsearch.senate.gov/search/view/extension-notice/regular/164a2035-198f-4fcd-9641-86af63a58c62/'
    meta = classify_doc_meta(t, u)
    assert meta['doc_type'] == 'Extension Notice'
    assert meta['doc_subtype'] == 'Annual Report'
    assert meta['doc_filetype'] == 'html'
    assert meta['amendment_number'] is 1
    assert meta['extension_number'] is 2
    assert meta['doc_related_date'] == '2015'
