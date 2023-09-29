#!/usr/bin/env python3

from bs4 import BeautifulSoup
from os import mkdir, walk
from os.path import dirname, exists, join, realpath


TITLE_SELECTOR = ".page-header__title-wrapper"
CONTENT_SELECTOR = "#content"


HERE = dirname(__file__)
SCRAPE_DIR = realpath(join(HERE, 'scraped'))
OUTPUT_DIR = realpath(join(HERE, 'parsed'))



for dirpath, dnames, fnames in walk(SCRAPE_DIR):
    for fname in fnames:
        if fname.endswith(".html"):
            html = open(join(dirpath, fname)).read()
            soup = BeautifulSoup(html, 'html.parser')      
            # try: 
            title = soup.css.select_one(TITLE_SELECTOR).text.strip()
            content = soup.css.select_one(CONTENT_SELECTOR).text.strip()
            fname = fname.replace('.html', '')
            outpath = join(OUTPUT_DIR, f"{fname}.txt")
            if exists(outpath):
                raise ValueError(f"dupe filename {outpath}")
            print(outpath)
            with open(outpath, 'w') as outfile:
                print(title, file=outfile)
                print("\n", file=outfile)
                print(content, file=outfile)
            # except AttributeError:
            #     print(f"error parsing '{join(dirpath, fname)}'")
            
