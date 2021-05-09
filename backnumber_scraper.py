import requests
from bs4 import BeautifulSoup

class BacknumberScraper:
  def __init__(self, url):
    self.url = url
    self.articles = []

  def scrape(self):
    self.fetch()
    self.parse()
  
  def fetch(self):
    html = requests.get(self.url)
    self.page = BeautifulSoup(html.content, "html.parser")

  def parse(self):
    elements = self.page.select("#box_mkj p,#box_mkj div,#box_mkj hr")
    current = []
    for element in elements:
      if element.name == "hr" or element.name == "div":
        if current:
          self.articles.append(current)
          current = []
      else:
        content = element.text.rstrip()
        current.append(content)
  
  def get_info(self):
    return self.articles
