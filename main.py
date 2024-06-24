import argparse

from src.scraper import Scraper

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--method", type=str, default='download')
    ap.add_argument("-mi", "--method_idx", type=str, default='download')
    args = vars(ap.parse_args())
    idx = args['method_idx']

    scraper = Scraper()
    if args['method'] == 'fix' or idx == 0:
      scraper.fix()
    elif args['method'] == 'download' or idx == 1:
      scraper.dl_initial_index_pages()
    elif args['method'] == 'parse_company_summaries' or idx == 2:
      scraper.parse_company_summaries()
    elif args['method'] == 'write_summaries_to_csv' or idx == 3:
      scraper.write_summaries_to_csv()
    elif args['method'] == 'dl_show_pages' or idx == 4:
      scraper.dl_show_pages()
    elif args['method'] == 'parse_job_links_from_index_pages' or idx == 5:
      scraper.parse_job_links_from_index_pages()
    elif args['method'] == 'parse_show_pages' or idx == 6:
      scraper.parse_show_pages()
    elif args['method'] == 'ms_start' or idx == 7:
      scraper.ms_start()
    