# __author__ = "Vasudev Gupta"

import bs4
import requests
import ast
import re

class Fetcher(object):
    
    def __init__(self, url= "http://www.arxiv-sanity.com/toptwtr"):
        self.url = url

    def fetch_papers(self):

        obj = requests.get(self.url)
        soup = bs4.BeautifulSoup(obj.content, "html.parser")
        
        content = soup('script')[6]
        content = str(content)
        content = re.split("\nvar papers = ", content)[1]
        content = re.split("\nvar pid_to_users = ", content)[0]
        content = ast.literal_eval(content[:-1])

        return content

    def dump(self, path=os.path.join("database", "top_tweets_based.pickle")):

        print("fetching trending papers based on yesterday's tweets ...", end=" ")
        papers = self.fetch_papers()
        num = len(papers)

        save_pickle(papers, path)
        print("||DONE||")
        print(f"Succesfully fetched {num} papers into database.")
