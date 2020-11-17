__author__ = "Vasudev Gupta"

import argparse
from utils import *

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fetch', action="store_true", help="fetches yesterday's trending papers based on tweets")
    parser.add_argument('-o', '--open_link', action='store_true', help="open link of best matching paper based on your query")
    args = parser.parse_args()

    if args.fetch:
        fetcher = Fetcher()
        fetcher.dumb()

    try:
        content = load_data()
    except:
        print("fetch database first")

    if args.open_link:
        open_link(content[0]['link'])