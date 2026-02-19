import requests
from bs4 import BeautifulSoup
import csv
import os

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        }
        self.folder_name = "Scraper"
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        self.response = requests.get(url= self.url, headers = self.headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def get_data(self):
        title = self.soup.find("span", {"id":"productTitle"}).text.strip()

        price = self.soup.find("span", {"class": "a-price-whole"}).text.strip()
        price_clean = int(price.replace(',', '').replace('.', ''))

        img_tag = self.soup.find("img",{"id": "landingImage"})
        img_url = img_tag["src"] if img_tag else None

        return {
            "Title": title,
            "Price": price_clean,
            "Image_Url": img_url
        }

    def save_to_csv(self, data):

        csv_path = os.path.join(self.folder_name, "prices.csv")
        file_exists = os.path.isfile(csv_path)
        with open(csv_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

    def download_image(self, img_url, name):

        if img_url:

            clean_name = "".join([c if c not in '<>:"/\\|?*' else "_" for c in name])
            clean_name = clean_name[:25]

            img_data = requests.get(img_url).content
            img_path = os.path.join(self.folder_name, f"{clean_name}.jpg")
            with open(img_path, 'wb') as f:
                f.write(img_data)


# tracker = PriceTracker(url = "https://www.amazon.in/Samsung-Smartphone-Icyblue-Snapdragon-ProVisual/dp/B0DSKMM5ZL/ref=sr_1_1?crid=1E5T375GJYWBZ&dib=eyJ2IjoiMSJ9.u3oNRuk1su5sLZB-iUGkvpOgFjrKqO1EPxBWNIqWBiG4H8o_8C-kM08MnwAVRS0YnqJgtKmVP2Dd-UkNVGBfSHZXlzdKYcc-9jy5eognkdfkkMke1KlHCFH8BwI9lmwlgLYtWr6W-AkA2aXzASt0C0g0Utorx3NcVVO-xOhUimCpD56hVc-19DOLpoKqa1MTK1DkgV_OPgHFIAdmy36qMHUzz11f5qBueve2OatFhkY.tK4KVsKShsNSMSjb2L154HveIhW_tmqGZQziwFvE6iQ&dib_tag=se&keywords=samsung%2Bgalaxy%2Bs25&qid=1771519656&sprefix=samsung%2Bgalaxy%2Bs2%2Caps%2C464&sr=8-1&th=1")
tracker = PriceTracker(url = "https://www.amazon.in/OnePlus-Infinite-Snapdragon%C2%AE-Personalised-Game-Changing/dp/B0FTRMJNPX/ref=pd_sbs_d_sccl_1_6/520-3352604-4808632?pd_rd_w=r80hQ&content-id=amzn1.sym.d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_p=d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_r=G3W5BV5H7VJSWF18A3SF&pd_rd_wg=KwSow&pd_rd_r=0b41ddc2-1e24-4cf6-a842-0259ca0fc903&pd_rd_i=B0FTRMJNPX&th=1")
product_info = tracker.get_data()

print(f"Scraped: {product_info['Title']}")
tracker.save_to_csv(product_info)
tracker.download_image(product_info['Image_Url'], product_info['Title'])
