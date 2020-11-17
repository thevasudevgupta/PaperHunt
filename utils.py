# @author: Vasudev Gupta

import bs4
import requests
import ast
import re
import pickle

import webbrowser
from tqdm import tqdm, trange

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

        print("fetching trending papers based on yesterday's tweets ...")
        papers = self.fetch_papers()
        num = len(papers)

        save_pickle(papers, path)
        print(f"||DONE|| Succesfully fetched {num} papers into database.")

def save_pickle(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)

def load_pickle(path="database.pickle"):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def open_link(link):
    print(f"opening {link} in your default browser")
    webbrowser.open(link)
