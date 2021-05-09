import time
import csv
from index_scraper import IndexScraper
from backnumber_scraper import BacknumberScraper

class Main:
  def __init__(self):
    self.domain = "http://lifescience.co.jp/"
    self.page_root_href = "yk/"
    self.index_page_href = "index_ykback.html"

  def exec(self):
    self.scrape_index_page()
    self.scrape_backnumbers()
    self.export_csv()
  
  def scrape_index_page(self):
    index_scraper = IndexScraper(self.domain + self.page_root_href + self.index_page_href)
    index_scraper.scrape()

    # 動作確認用
    self.years = [index_scraper.get_info()[0]]
    # self.years = index_scraper.get_info()
  
  def scrape_backnumbers(self):
    for year in self.years:
      for backnumber in year["backnumbers"]:
        href = backnumber["href"]
        print(self.domain + self.page_root_href + href)
        backnumber_scraper = BacknumberScraper(self.domain + self.page_root_href + href)
        backnumber_scraper.scrape()
        backnumber["articles"] = backnumber_scraper.get_info()
        time.sleep(1)
  
  def export_csv(self):
    csv_header = ['year', 'backnumber','title', 'other1', 'other2', 'other3']
    csv_body = []
    for year in self.years:
      for backnumber in year["backnumbers"]:
        for article in backnumber["articles"]:
          csv_body.append([year["name"], backnumber["name"], article["title"], *article["others"]])

    with open('result.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerow(csv_header)
      writer.writerows(csv_body)

if __name__ == "__main__":
  Main().exec()