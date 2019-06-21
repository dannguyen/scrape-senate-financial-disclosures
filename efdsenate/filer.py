from pathlib import Path


DATA_PATH = Path('data')

STASHED_DIR = DATA_PATH / 'stashed'
PARSED_DIR = DATA_PATH / 'parsed'
DOCFILES_DIR = DATA_PATH / 'docfiles'


def docfile_index_path(id, doc_filetype):
    if doc_filetype == 'html':
        return DOCFILES_DIR / (id + '.html')
    elif doc_filetype == 'paper':
        return DOCFILES_DIR / id / 'index.html'
    else:
        raise ValueError("Unexpected docfiletype value: {}".format(doc_filetype))

def make_inventory():
    pass
    """
    toplevel function to create a CSV of all expected:
        HTML filings:
            - HTML file
            - attachments
        Paper filings:
            - HTML file
            - GIFs

        And record:
            - type, e.g. html-index, paper-image, attachment
            - current file location on disk, if any
            - remote url
            - size in bytes
            - HTTP status, e.g. 200, 404, 503
            - file modified time
            - linkage to: first_name, last_name, doc_type, date, doc-title

    Effects:
        produce data/docfiles-inventory.csv
    """
