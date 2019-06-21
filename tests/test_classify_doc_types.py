from efdsenate.scraping.raw_parser import _classify_doc_type
import pytest


def test_classify_doc_types_as_fdreports():
    titles = ['Some Annual Report', 'The Termination Report',
            'New Filer Report (Amendment 9)', 'Candidate Report for funzies']
    for t in titles:
        dt = _classify_doc_type(t, 'http://example.com/something/view/paper/sadfklj')
        assert dt == 'Financial Disclosure Report'

def test_classify_doc_types_as_extensions():
    titles = ['Some Annual Report Due Date Extension', 'The Extension Termination Report',
            'Extension Notice for Periodic Transaction REports', 'Candidate Report Extension']
    for t in titles:
        dt = _classify_doc_type(t, 'http://example.com/something/view/paper/sadfklj')
        assert dt == 'Extension Notice'


def test_classify_doc_types_as_misc():
    dt = _classify_doc_type('Miscellaneous Info', 'example.com')
    assert dt == 'Miscellaneous Information'

    dt = _classify_doc_type('Miscellaneous Due Date Extension', 'example.com')
    assert dt == 'Miscellaneous Information'

    dt = _classify_doc_type('Blind Trust Report', 'example.com')
    assert dt == 'Blind Trust'

    dt = _classify_doc_type('Blind Trust Due Date Extension', 'example.com')
    assert dt == 'Blind Trust'


def test_clasify_doc_types_as_ptr():
    dt = _classify_doc_type('Periodic Transaction Report for 06/19/2018', 'url')
    assert dt == 'Periodic Transaction Report'

    # existence of view/ptr in URL is NOT used to classify PTRs
    dt = _classify_doc_type('Perioidic Annual Report for 09/09/2009', 'http://example.com/view/ptr/stuff')
    assert dt == 'Financial Disclosure Report'

    with pytest.raises(ValueError, match='did not match an expected doc_type'):
        dt = _classify_doc_type('Periodic Transaction for 06/19/2018', 'url')
