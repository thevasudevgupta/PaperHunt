# @author: Vasudev Gupta

import bs4
import requests
import ast
import re
import pickle

import webbrowser

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

    def dumb(self, path="database.pickle"):

        f = open(path, 'wb')

        papers = self.fetch_papers()
        num = len(papers)

        pickle.dump(papers, f)
        print(f"fetched trending {num} papers based on yesterday's tweets")
        f.close()

def load_data(path="database.pickle"):
    
    with open(path, 'rb') as f:
        papers = pickle.load(f)

    return papers

def open_link(link):
    print(f"opening {link} in your default browser")
    webbrowser.open(link)
