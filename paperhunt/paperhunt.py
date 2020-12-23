__author__ = "Vasudev Gupta"

import os
import argparse

import warnings
warnings.filterwarnings("ignore")

from paperhunt.utils import open_link, load_pickle, save_pickle, makedirs
from paperhunt.search_engine import SpacySearchEngine, BM25SearchEngine

def main():
    parser = argparse.ArgumentParser("This tool enables fetching recent papers using CLI")
    parser.add_argument('-f', '--fetch', action="store_true", help="whether to fetch papers in database")
    parser.add_argument('-o', '--open_link', action='store_true', help="open link of best matching paper based on your query")
    parser.add_argument('-q', '--query', type=str, help="get papers based on your interest by specifying your type")
    parser.add_argument('-n', '--num_papers',type=int, default=1, help="specify # of papers you want to read")
    parser.add_argument("--category", type=str, default="top_tweets_based", help="choose something out of top_tweets_based, emnlp2020")
    args = parser.parse_args()

    if args.category == "emnlp2020":
        from paperhunt.sites.emnlp import Fetcher
    elif args.category == "top_tweets_based":
        from paperhunt.sites.arxiv_sanity import Fetcher
    else:
        raise ValueError("specified category is not valid")

    m = None
    makedirs("database")

    if args.fetch:
        try:
            fetcher = Fetcher()
            fetcher.dump()
        except:
            m = "website server is down"
            print(m)

    if not m:

        if f"{args.category}.pickle" not in os.listdir("database"):
            raise ValueError(f"Couldn't load database || FIRSTLY fetch {args.category} database in current directory")

        if args.query:
            print("loading database of papers")
            content = load_pickle(os.path.join("database", f"{args.category}.pickle"))
            engine = BM25SearchEngine(content)
            best_content = engine.return_best_info(args.query, args.num_papers)

        # if args.open_link:
        #     try:
        #         for bc in best_content:
        #             open_link(bc['link'])
        #     except:
        #         print("Nothing is there in best content")


if __name__ == '__main__':
    main()