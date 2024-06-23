import time
import requests

from .constants import urls, headers
from .utils import setup_logger, dl_dir

class Scraper():
    def __init__(self):
        self.logger = setup_logger()

    def log(self, val):
        self.logger.info(val)

    def download_all(self):
        self.all_pages = []
        sites = urls.keys()
        for _, company in enumerate(sites):
            pages = urls[company]
            for idx, page in enumerate(pages):
                response = requests.get(page, headers=headers)
                filename = f"{dl_dir}/{company}-{idx}.html"
                with open(filename, 'wb') as f:
                    content = response.content
                    f.write(content)
                    self.all_pages = content
                print(f"File downloaded: {filename}")
                time.sleep(2)
                
