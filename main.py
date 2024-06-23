import sys
import time
import argparse

from src.scraper import Scraper

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-dl", "--download", type=str, default='download')
    args = vars(ap.parse_args())

    fn_name = args['download']
    if fn_name == 'download':
      scraper = Scraper()
      scraper.download_all()