# __author__ = "Vasudev Gupta"

import spacy
import pandas as pd
from tqdm import tqdm


class SearchEngine(object):

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
