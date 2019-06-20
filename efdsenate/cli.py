from argparse import ArgumentParser
import csv
import json

from pathlib import Path
import re
from sys import stderr, stdout
import traceback
from urllib.parse import urljoin
from constants import DATA_PATH, BASE_DOMAIN
from constants import US_STATES
from constants import hparse

from scraper import scrape_by_state, init_scraper
from raw_parser import parse_raw_records, PARSED_HEADERS

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

def main():
    parser = init_arg_parser()
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






def fetch_files():
    scraper, _x = init_scraper()
    records = list(csv.DictReader(open(PARSED_DIR / 'state-indexes.csv')))
    # records = [r for r in records if 'view/paper' in r['doc_url']] # TEMPTHING
    records = [r for r in records if r['doc_id']]
    for n, r in enumerate(records):
        print('{}. '.format(n), r['last_name'], r['first_name'], r['date'], r['doc_title'])


        url = r['doc_url']
        id = r['doc_id']

        if 'view/paper' not in url:
            destname = DOCFILES_DIR / (id + '.html')
            if not destname.exists():
                resp = scraper.get(url)
                if resp.status_code == 200:
                    destname.parent.mkdir(parents=True, exist_ok=True)
                    destname.write_text(resp.text)
                    print(n, ' - Wrote', len(resp.text), 'chars to:', destname)
        else:
            print("\t\t\t\t....paper!")
            destname = DOCFILES_DIR / id / 'index.html'
            destdir = destname.parent
            destdir.mkdir(parents=True, exist_ok=True)

            if not destname.exists():
                print(destname)
                resp = scraper.get(url)


                if resp.status_code == 200:
                    doc = hparse(resp.text)
                    imgs = doc.cssselect('img.filingImage')
                    img_counter = 0

                    try:
                        for img in imgs:
                            href = img.attrib['src']
                            img_url = urljoin(BASE_DOMAIN, href)
                            print("\t getting image: ", img_url)
                            ix = scraper.get(img_url)
                            if ix.status_code == 200:
                                dest_imgname = destdir / Path(href).name
                                print("\t saving to: ", dest_imgname)
                                dest_imgname.write_bytes(ix.content)

                            else:
                                raise IOError("Did not get status code 200 for URL: {}".format(img_url))
                    except Exception as err:
                        print("Failed when trying to get images for {}: {}/{}".format(destname,
                            img_counter, len(imgs)))
                        print(err)
                    else:
                        destname.write_text(resp.text)
                        print(n, ' - (paper) Wrote', len(resp.text), 'chars to:', destname)
                        print('----')

                    # now for the image extraction





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

    allrecs = sorted(allrecs,
                     key=lambda r: [r['state'], r['last_name'], r['first_name'],
                            r['date'], r['doc_type'], r['amendment_number'], r['extension_number']
                        ])

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

#####################
if __name__ == '__main__':
    main()


