import argparse
import logging
from dalle3_api import *

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bing Image Creator Downloader (Dalle-3)")
    parser.add_argument("query", type=str, help="Search query for Bing Image Creator (Dalle-3)")
    args = parser.parse_args()
    query = args.query

    logging.info(f'{get_time()} Program started')

    open_website(query)

    urls = get_urls()

    download_images(urls, query)
