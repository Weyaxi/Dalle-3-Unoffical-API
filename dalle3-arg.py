import argparse
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bing Image Creator Downloader (Dalle-3)")
    parser.add_argument("queries", type=str, nargs='+', help="Search queries for Bing Image Creator (Dalle-3)")
    args = parser.parse_args()
    queries = args.queries

    from dalle3_api import *  # The import is here because we don't need to import functions and open the webdriver if there is an error in the arguments.

    logging.info(f'{get_time()} Program started')

    for query in queries:
        open_website(query)
        urls = get_urls()
        download_images(urls, query)
