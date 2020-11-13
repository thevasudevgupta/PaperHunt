"""Scrapping papers from arxiv

@author: vasudevgupta
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# pip install webdriver-manager
# from webdriver_manager.chrome import ChromeDriverManager

class Scrapper(object):
    
    def __init__(self, 
                 url= "https://arxiv.org/list/cs.CL/new", 
                 driver_path= "/Users/vasudevgupta/.wdm/drivers/chromedriver/mac64/83.0.4103.39/chromedriver"):
        
        driver_path = '/usr/local/chromedriver'
        # driver_path = ChromeDriverManager().install()
        self.driver= webdriver.Chrome(driver_path)
        
        # self.driver.maximize_window()
        
        self.driver.get(url)
    
    def scrap_single_paper(self, idx):
        """
        Run this to extract info for one paper based on index
        """
        # item no
        path = f"//div[@id='dlpage']/dl/dt{[idx]}/a[@name='item{idx}']"
        item_no = self.driver.find_element_by_xpath(path).get_attribute('name')
        
        # paper link
        path = f"//div[@id='dlpage']/dl/dt{[idx]}/span[@class='list-identifier']/a[@title='Abstract']"
        paper_link = self.driver.find_element_by_xpath(path).get_attribute('href')

        # paper name
        path = f"//div[@id='dlpage']/dl/dd{[idx]}/div[@class='meta']/div[@class='list-title mathjax']"
        paper_name = self.driver.find_element_by_xpath(path).text

        # authors name
        path = f"//div[@id='dlpage']/dl/dd{[idx]}/div[@class='meta']/div[@class='list-authors']"
        authors_name = self.driver.find_element_by_xpath(path).text
            
        # paper abstract
        path = f"//div[@id='dlpage']/dl/dd{[idx]}/div[@class='meta']/p[@class='mathjax']"
        abstract = self.driver.find_element_by_xpath(path).text
        
        keys = ['item-no', 'paper-link', 'paper-name', 'authors-name', 'abstract']
        values = [item_no, paper_link, paper_name, authors_name, abstract]
        
        info = dict(zip(keys, values))
        return info
    
    def scrap_multiple_papers(self, max_papers):
        
        ls = []
        
        for idx in range(1, max_papers):
        
            info= self.scrap_single_paper(idx)
            ls.append(info)
        
        return ls
            
if __name__ == '__main__':
    
    url= "https://arxiv.org/list/cs.CL/new"

    scrapper = Scrapper(url)
    ls = scrapper.scrap_multiple_papers(4)

    
    


