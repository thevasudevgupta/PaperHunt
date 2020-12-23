# __author__ = "Vasudev Gupta"

import bs4
import requests
from tqdm import tqdm

from utils import save_pickle

class Fetcher(object):
    
    def __init__(self, url= "https://2020.emnlp.org/papers/main"):
        self.url = url

    def fetch_papers(self):

        obj = requests.get(self.url)
        soup = bs4.BeautifulSoup(obj.content, "html.parser")        
        web = soup.find_all("li", class_="single-paper-wrapper")
        total = len(web)

        content = []
        for c in tqdm(web, desc="fetching ... ", total=total, leave=False):
            content.append({"title": c["title"].split(":")[0],
                        "abstract": c["title"],
                        "authors": c.find("span", class_="paper-authors").text})

        return content

    def dump(self, path=os.path.join("database", "emnlp2020.pickle")):

        print("fetching emnlp2020 papers ...", end=" ")
        papers = self.fetch_papers()
        num = len(papers)

        save_pickle(papers, path)
        print("||DONE||")
        print(f"Succesfully fetched {num} emnlp2020 papers into database.")
