__author__ = "Vasudev Gupta"

import os
import argparse
from utils import *

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':

    parser = argparse.ArgumentParser("Control what you read from command line")
    parser.add_argument('-f', '--fetch', action="store_true", help="fetches yesterday's trending papers based on tweets")
    parser.add_argument('-o', '--open_link', action='store_true', help="open link of best matching paper based on your query")
    parser.add_argument('-q', '--query', type=str, help="get papers based on your interest by specifying your type")
    parser.add_argument('--k', type=int, default=1, help="how many best papers to get")
    args = parser.parse_args()

    m = None

    if args.fetch:
        try:
            fetcher = Fetcher()
            fetcher.dumb()
        except:
            m = "server of arxiv-sanity is down"
            print(m)

    if not m:

        if "database.pickle" not in os.listdir():
            raise ValueError("Couldn't load database || FIRSTLY fetch database in current directory")

        if args.query:
            print("loading database of papers")
            content = load_pickle()
            query = Query()
            best_content = query.return_best_info(args.query, content, args.k)

        if args.open_link:
            try:
                for bc in best_content:
                    open_link(bc['link'])
            except:
                print("Nothing is there in best content")
