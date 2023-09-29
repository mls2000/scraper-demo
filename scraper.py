#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from time import sleep
from os import mkdir, makedirs
from os.path import dirname, exists, join, abspath


''' this is the website we will scrape '''
URL = "https://avatar.fandom.com/wiki/"

URL_LENGTH = len(URL)
PARSED = urlparse(URL)
DOMAIN = f"{PARSED.scheme}://{PARSED.netloc}"
PATH = PARSED.path
PATH_LENGTH = len(PATH) if len(PATH.replace('/', '')) > 0 else 0


LINKS = set(URL)
QUEUE = [URL]

WAIT_SECONDS = 1

'''
make the output destination predictable, regardless of where you
call it from
'''
HERE = dirname(__file__)
OUTPUT_DIR = abspath(join(HERE, 'scraped'))


def process_next():
    while len(QUEUE) > 0:
        url = QUEUE.pop(0)
        download(url)
        sleep(WAIT_SECONDS)


def download(url):
    print(f"fetching '{url}'")
    try: 
        r = requests.get(url)
        page_links = get_links(r.text, url)
        filepath = get_filepath_from_url(url)
        try:
            with open(filepath, 'w') as outfile:
                outfile.write(r.text)
        except OSError as ose:
            print(f"could not save '{filepath}' for {url}")
            raise()
        for link in page_links: 
            if link not in LINKS:
                LINKS.add(link)
                QUEUE.append(link)
    except requests.ConnectionError as ce:
        print(f"could not fetch '{url}'", ce)


def get_filepath_from_url(url):
    if url == URL: 
        filepath = 'index'
    elif url.startswith(URL):
        ''' 
        strip the domain from the url. For example, if our target site is 
          http://www.webpage.com/a/bunch/of/folders
        and the current url is 
          http://www.webpage.com/a/bunch/of/folders/to/a/file.html
        we want the 
          to/a/file.html
        part. 
        '''
        filepath = url[URL_LENGTH:]
    '''
    we don't want a leading '/' in the filepath, because 
    if we try to add it to OUTPUT_DIR, it can break out 
    and make stuff go to the root directory
    '''
    if filepath[0] == '/':
        filepath = filepath[1:]
    '''
    separate the folders from the last part of the path, 
    which will become the file name. 
    For example, if filepath is now 
      to/a/file.html
    we want to split "to/a" from "file.html"
    '''
    last_slash = filepath.rfind('/')
    if last_slash > 0:
        filename = filepath[last_slash + 1:]
        filepath = filepath[0: last_slash]
    else: 
        filename = filepath
        filepath = ''
    if not filename.endswith('.html'): 
        filename += '.html'
    outpath = join(OUTPUT_DIR, filepath)
    if not exists(outpath):
        makedirs(outpath)
    return join(OUTPUT_DIR, filepath, filename)

    
def get_links(html, baseurl):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        '''
        Here's a little safety check: there may be links where the href never gets set. 
        Sadly your scraper may have to work around poorly formed HTML like this.
        '''
        if href:
            if "?" in href: 
                href = href[0: href.find("?")]
            if href.lower().startswith("http"):
                '''
                The link starts with the full website. Is it the one we want? 
                '''
                if href.startswith(URL):
                    ''' this is an absolute url that lives under our target site '''
                    links.append(href)
            elif href.lower().startswith(f"//{PARSED.netloc}"):
                ''' urls can start with the double slash instead of specifying "https" or "http" '''
                href = f"{PARSED.scheme}:{href}"
                if href.startswith(URL):
                    ''' this is an absolute url that lives under our target site '''
                    links.append(href)
            elif href.startswith('#'): 
                ''' skip it, it's just another part of the same html file '''
                pass
            elif '/' == href[0]:
                if PATH_LENGTH == 0: 
                    ''' our target is the root domain of the site '''
                    links.append(DOMAIN + href)  
                elif href[0: PATH_LENGTH] == PATH:
                    ''' 
                    our target is a folder somewhere below the root domain of the site, 
                    but the path here matches it
                    '''
                    links.append(DOMAIN + href)
            else:
                ''' 
                this link is relative to the url that we were just on 
                '''
                if baseurl.endswith('/'): 
                    links.append(baseurl + href)
                elif baseurl.endswith('.html'): 
                    last_slash = baseurl.rfind('/')
                    links.append(f"{baseurl[0:last_slash]}/{href}")
                    print(f"transformed {href} and {baseurl} into {baseurl[0:last_slash]}/{href}")
                else: 
                    links.append(f"{baseurl}/{href}")
    return links



if __name__ == "__main__":
    process_next()
    import sys
    sys.exit(0)