# __author__ = "Vasudev Gupta"

from rank_bm25 import BM25Okapi
import spacy
import pandas as pd
from tqdm import tqdm


class SpacySearchEngine(object):

    def __init__(self, content):
        
        self.content = content
        self.nlp = spacy.load('en_core_web_md')

        print("Initiating the search engine")

    def _get_scores(self, q):

        scores = []
        titles = []
        q = self.nlp(q)

        bar = tqdm(enumerate(self.content), desc="matching similarity .. ", leave=True, total=len(self.content))
        for i, d in bar:
            titles.append((d["title"], i))
            paper = self.nlp(d["title"])
            score = q.similarity(paper)
            scores.append(score)
        return pd.Series(data=scores, index=titles)

    def return_best_info(self, q, n=2):
        papers = self._get_scores(q)
        papers = papers.nlargest(n=n)
        indices = [i for _,i in papers.index]
        print("======= MATCHING PAPERS ARE =======")
        for p in papers: print(p)
        print("===================================")
        return [self.content[i] for i in indices]

class BM25SearchEngine(object):

    def __init__(self, content):

        self.content = content
        tokenized_content = [doc["abstract"].lower().split() for doc in content]
        self.bm25 = BM25Okapi(tokenized_content)

        print("Initiating the search engine")

    def return_best_info(self, q, n=2):
        tokenized_query = q.lower().split()
        papers = self.bm25.get_top_n(tokenized_query, [doc["title"] for doc in self.content], n=n)
        print("======= MATCHING PAPERS ARE =======")
        for p in papers: print(p)
        print("===================================")
