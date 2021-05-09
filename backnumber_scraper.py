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
      # href = link_element["href"]
      others = self.get_other_info([], parent)
      article_info = { "title": title, "others": others }
      self.articles.append(article_info)
  
  def get_other_info(self, others, current):
    next = current.next_sibling
    if next == None or next.name == "hr" or next.name == "div":
      return others

    if next.name == "p":
      others.append(next.string)
      self.get_other_info(others, next)
    else:
      self.get_other_info(others, next)

    return others
  
  def get_info(self):
    return self.articles
