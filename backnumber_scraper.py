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
    link_elements = self.page.select("#box_mkj p a")
    for link_element in link_elements:
      parent = link_element.find_parent("p")
      title = parent.text.rstrip()
      href = link_element["href"]
      article_info = { "title": title, "href": href }
      self.articles.append(article_info)
  
  def get_info(self):
    return self.articles
