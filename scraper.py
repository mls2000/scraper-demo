#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from time import sleep


''' this is the website we will scrape '''
URL = "https://avatar.fandom.com/wiki/"

URL_LENGTH = len(URL)
PARSED = urlparse(URL)
DOMAIN = f"{PARSED.scheme}://{PARSED.netloc}"
PATH = PARSED.path
PATH_LENGTH = len(PATH) if len(PATH.replace('/', '')) > 0 else 0


''' 
Track the links we have visited, so we don't visit the same link twice, 
lest we get caught in an endless loop.
'''
LINKS = set(URL)
QUEUE = [URL]


WAIT_SECONDS = 1


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
        for link in page_links: 
            if link not in LINKS:
                LINKS.add(link)
                QUEUE.append(link)
                print(f"{url} links to {link}")
    except requests.ConnectionError as ce:
        print(f"could not fetch '{url}'", ce)


    
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