"""
a collection of public-facing methods mostly meant to be used by the CLI
"""
import csv
import json
from pathlib import Path
import re
from sys import stderr, stdout
from urllib.parse import urljoin


from constants import US_STATES, BASE_DOMAIN
import filer
from filer import STASHED_DIR, PARSED_DIR, DOCFILES_DIR
from helpers import hparse

from scraping.fetcher import scrape_by_state, init_scraper
from scraping.raw_parser import parse_raw_records, PARSED_HEADERS
from scraping.raw_extractor import  _extract_image_urls_from_paper_file



def fetch_doc_files():
    """
     brute force scrape of all associated files given a doc_url, including
     the html, gifs (if it's a paper form), and (TODO) attachments
    """

    scraper, _x = init_scraper()
    records = list(csv.DictReader(open(PARSED_DIR / 'state-indexes.csv')))
    # records = [r for r in records if 'view/paper' in r['doc_url']] # TEMPTHING
    records = [r for r in records if r['doc_id']]
    for n, r in enumerate(records):
#        print('{}. '.format(n), r['last_name'], r['first_name'], r['date'], r['doc_title'])


        url = r['doc_url']
        id = r['doc_id']

        if 'view/paper' not in url:
            destname = filer.docfile_index_path(id, 'html')
            if not destname.exists():
                print('{}. '.format(n), r['last_name'], r['first_name'], r['date'], r['doc_title'])
                resp = scraper.get(url)
                if resp.status_code == 200:
                    destname.parent.mkdir(parents=True, exist_ok=True)
                    destname.write_text(resp.text)
                    print(n, ' - Wrote', len(resp.text), 'chars to:', destname)
                else:
                    print("\tDid not get status code 200; Got status code {} for URL: {}".format(resp.status_code, resp.url))

        else:
            # it's paper time!
#            print("\t\t\t\t....paper!")
            destname = filer.docfile_index_path(id, 'paper')
            destdir = destname.parent
            destdir.mkdir(parents=True, exist_ok=True)

            if not destname.exists():
                # print(destname)
                print('{}. '.format(n), r['last_name'], r['first_name'], r['date'], r['doc_title'])
                resp = scraper.get(url)


                if resp.status_code == 200:

                    imgs = _extract_image_urls_from_paper_file(resp.text)
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
                            elif ix.status_code == 404:
                                print("\t 404 for this image...oh well")
                            else:
                                raise IOError("\tDid not get status code 200/404; Got status code {} for URL: {}".format(ix.status_code, img_url))
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






def fetch_and_stash_allstates():
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




def collate_state_indexes():
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


def collate_docfiles():
    import formparser
    formparser.main()
