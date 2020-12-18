# __author__ = "Vasudev Gupta"

import bs4
import requests
import ast
import re
import pickle

import spacy
import pandas as pd

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

        print("fetching trending papers based on yesterday's tweets ...", end=" ")
        papers = self.fetch_papers()
        num = len(papers)

        save_pickle(papers, path)
        print("||DONE||")
        print(f"Succesfully fetched {num} papers into database.")

class Query(object):

    def __init__(self):
        
        try:
            self.nlp = spacy.load('en_core_web_md')
        except:
            print("Run `source entrypoint.sh` first")

        print("Initiating the search engine")

    def get_scores(self, q, content):

        scores = []
        titles = []
        q = self.nlp(q)

        bar = tqdm(enumerate(content), desc="matching similarity .. ", leave=True, total=len(content))
        for i, d in bar:
            titles.append((d["title"], i))
            paper = self.nlp(d["title"])
            score = q.similarity(paper)
            scores.append(score)
        return pd.Series(data=scores, index=titles)

    def return_best_info(self, q, content, k=2):
        papers = self.get_scores(q, content)
        papers = papers.nlargest(n=k)
        indices = [i for _,i in papers.index]
        print("======= MATCHING PAPERS ARE =======")
        _ = [print(p) for p,_ in papers.index]
        print("===================================")
        return [content[i] for i in indices]

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
