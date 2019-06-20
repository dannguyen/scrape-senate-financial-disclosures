from argparse import ArgumentParser
import csv
import json

from pathlib import Path
import re
from sys import stderr, stdout
import traceback

from constants import DATA_PATH
from constants import US_STATES
from scraper import scrape_by_state, init_scraper
from parser import parse_raw_records, PARSED_HEADERS

STASHED_DIR = DATA_PATH / 'stashed'
PARSED_DIR = DATA_PATH / 'parsed'
DOCFILES_DIR = DATA_PATH / 'docfiles'


def _define_subparsers(parser):
    subparsers = parser.add_subparsers()
    wparser = subparsers.add_parser('state', help='For a given state, retrieve all the filings')
    wparser.set_defaults(mode='state')
    wparser.add_argument('state', help='''the postal code of the state, e.g. NY, FL''')


    wparser = subparsers.add_parser('parse_raw', help='Parse extracted records into one nice CSV')
    wparser.set_defaults(mode='parse_raw')

    wparser = subparsers.add_parser('fetch_files', help='Fetch files from parsed CSV')
    wparser.set_defaults(mode='fetch_files')
    return subparsers


def init_arg_parser():
    mainparser = ArgumentParser(description="Scrape and wrangle US Senate financial disclosures")
    mainparser.set_defaults(mode='main')
    _define_subparsers(mainparser)
    return mainparser

def process_parsed_args(parser):
    args = parser.parse_args()
    if args.mode == 'main':
        # do nothing but print the help to screen
        parser.print_help()
    elif args.mode == 'fetch_files':
        fetch_files()
    elif args.mode == 'parse_raw':
        parse_raw_indexes()
    elif args.mode == 'state':
        if args.state == '':
            stash_allstates()
        else:
            fetch_state_index(args.state)


def main():
    p = init_arg_parser()
    process_parsed_args(p)


#####################
if __name__ == '__main__':
    main()







def fetch_files():
    scraper, _x = init_scraper()
    records = list(csv.DictReader(open(PARSED_DIR / 'state-indexes.csv')))
    for n, r in enumerate(records):
        url = r['doc_url']
        id = r['doc_id']
        if 'view/paper' not in url and id:
            destname = DOCFILES_DIR / (id + '.html')
            if not destname.exists():
                resp = scraper.get(url)
                if resp.status_code == 200:
                    destname.parent.mkdir(parents=True, exist_ok=True)
                    destname.write_text(resp.text)
                    print(n, ' - Wrote', len(resp.text), 'chars to:', destname)


def fetch_state_index(state_initials):
    scraper, responses, records = scrape_by_state(state_initials)

    stderr.write(state_initials + "\n")

    stdout.write(json.dumps(records, indent=2))

    stderr.write('Responses: {}\n'.format(len(responses)))
    stderr.write('Records: {}\n'.format(len(records)))


def parse_raw_indexes():
    allrecs = []
    srcdir = STASHED_DIR / 'state-indexes'
    srcfiles = srcdir.glob('*.json')
    for s in srcfiles:
        print(s)
        rawrecs = json.loads(s.read_text())
        recs = parse_raw_records(rawrecs)
        for r in recs:
            r['state'] = s.stem
            allrecs.append(r)

    allrecs = sorted(allrecs, key=lambda r: [r['state'], r['last_name'], r['first_name'], r['date'], r['doc_type']])

    destpath = PARSED_DIR / 'state-indexes.csv'
    destpath.parent.mkdir(parents=True, exist_ok=True)
    with destpath.open('w') as w:
        c = csv.DictWriter(w, fieldnames=PARSED_HEADERS)
        c.writeheader()
        c.writerows(allrecs)

    print("Wrote", len(allrecs), 'records to:\n', destpath)

def stash_allstates():
    allrecs = []
    outdir = STASHED_DIR / 'state-indexes'

    for state in US_STATES:
        stderr.write("\n{}\n--\n".format(state))
        scraper, responses, records = scrape_by_state(state)

        stderr.write('- Records: {}\n'.format(len(records)))

        allrecs.extend(records)

        outpath = outdir / "{}.json".format(state)
        print(outpath)

        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(json.dumps(records, indent=2))

    stderr.write("\n=================\n")
    stderr.write('- Total records: {}\n'.format(len(allrecs)))


if __name__ == "__main__":
    main()
