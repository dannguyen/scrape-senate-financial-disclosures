from argparse import ArgumentParser
from pathlib import Path
import re
from sys import stderr, stdout
import traceback

from constants import DATA_PATH
from constants import US_STATES
from scraper import scrape_by_state


def _define_subparsers(parser):
    subparsers = parser.add_subparsers()
    wparser = subparsers.add_parser('state', help='For a given state, retrieve all the filings')
    wparser.set_defaults(mode='state')
    wparser.add_argument('state', help='''the postal code of the state, e.g. NY, FL''')

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

    elif args.mode == 'state':
        if args.state == '':
            stash_all_states()
        else:
            fetch_state(args.state)


def main():
    p = init_arg_parser()
    process_parsed_args(p)


#####################
if __name__ == '__main__':
    main()


import json
def fetch_state(state_initials):
    scraper, responses, records = scrape_by_state(state_initials)

    stderr.write(state_initials + "\n")

    stdout.write(json.dumps(records, indent=2))

    stderr.write('Responses: {}\n'.format(len(responses)))
    stderr.write('Records: {}\n'.format(len(records)))

def stash_all_states():
    allrecs = []
    outdir = DATA_PATH / 'state-indexes'

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
