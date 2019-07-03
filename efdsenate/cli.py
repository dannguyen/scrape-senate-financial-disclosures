from argparse import ArgumentParser
from scraper import fetch_doc_files, fetch_state_index
from scraper import fetch_and_stash_allstates, collate_state_indexes, collate_docfiles





def _define_subparsers(parser):
    subparsers = parser.add_subparsers()
    wparser = subparsers.add_parser('state', help='For a given state, retrieve all the filings')
    wparser.set_defaults(mode='state')
    wparser.add_argument('state', help='''the postal code of the state, e.g. NY, FL''')


    wparser = subparsers.add_parser('collate_states', help='Parse extracted records into one nice CSV')
    wparser.set_defaults(mode='collate_states')

    wparser = subparsers.add_parser('collate_docs', help='Parse extracted records into one nice CSV')
    wparser.set_defaults(mode='collate_docs')

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
        fetch_doc_files()
    elif args.mode == 'state':
        if args.state == '':
            fetch_and_stash_allstates()
        else:
            fetch_state_index(args.state)

    elif args.mode == 'collate_states':
        collate_state_indexes()


    elif args.mode == 'collate_docs':
        collate_docfiles()






#####################
if __name__ == '__main__':
    main()


