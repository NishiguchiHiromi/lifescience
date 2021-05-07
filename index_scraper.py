import requests
from bs4 import BeautifulSoup

class IndexScraper:
  def __init__(self, url):
    self.url = url
    self.years = []

  def scrape(self):
    self.fetch()
    self.parse()
  
  def fetch(self):
    html = requests.get(self.url)
    self.page = BeautifulSoup(html.content, "html.parser")

  def parse(self):
    year_elements = self.page.select("#boxbn dl")
    for year_element in year_elements:
      year_parser = YearParser(year_element)
      year_parser.parse()
      self.years.append(year_parser.get_info())
  
  def get_info(self):
    return self.years





class YearParser:
  def __init__(self, element):
    self.element = element
    self.backnumbers = []
  
  def parse(self):
    self.name = self.element.select_one("dt").get_text()
    link_elements = self.element.select("a")
    for link_element in link_elements:
      name = link_element.get_text()
      href = link_element['href']
      backnumber_info = { "name": name, "href": href }
      self.backnumbers.append(backnumber_info)
  
  def get_info(self):
    return { "name": self.name, "backnumbers": self.backnumbers }


