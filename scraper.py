#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from os import mkdir, makedirs
from os.path import dirname, exists, join, abspath
from urllib.parse import urlparse


HERE = dirname(__file__)
OUTPUT_DIR = abspath(join(HERE, 'scraped'))


URL = "https://avatar.fandom.com/wiki/"
''' 
While parsing links on the site, we will need to handle both 
absolute (http://site/subfolder) and relative (/subfolder/) links. 

And when we convert the path into a filename, it will be handy to 
know the length of the url as a string, in order to quickly remove
it from the file path

'''
URL_LENGTH = len(URL)
''' grab the various part'''
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


def process_next():
  while len(QUEUE) > 0:
    url = QUEUE.pop(0)
    download_and_save(url)


def download_and_save(url):
    print(f"fetching '{url}'")
    try: 
      r = requests.get(url)
      filepath = get_filepath_from_url(url)
      with open(filepath, 'w') as outfile:
        outfile.write(r.text)
      page_links = get_links(r.text)
      for link in page_links: 
        if link not in LINKS:
          LINKS.add(link)
          QUEUE.append(link)
    except requests.ConnectionError:
      print(f"could not fetch '{url}'")
    

def get_filepath_from_url(url):
    if url == URL: 
        filepath = 'index'
    elif url.startswith(URL):
        ''' the url is an absolute path, so trim the beginning part '''
        filepath = url[URL_LENGTH:]
    else: 
        ''' the url is a relative path '''
        filepath = url
    '''
    we don't want a leading '/' in the filepath, because 
    if we try to add it to OUTPUT_DIR, it can break out 
    and make stuff go to the root directory
    '''
    if filepath[0] == '/':
      filepath = filepath[1:]
    path_tokens = filepath.split('/')
    ''' separate the file name from the folders in the path '''
    filepath = "/".join(path_tokens[0:-1])
    filename = path_tokens[-1]
    if not filename.endswith('.html'): 
        filename += '.html'
    outpath = join(OUTPUT_DIR, filepath)
    if not exists(outpath):
        makedirs(outpath)
    return join(OUTPUT_DIR, filepath, filename)
    

  
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
      href = link.get('href')
      if href: 
        if href.startswith(URL):
          ''' this is an absolute url that lives under our target site '''
          links.append(href)
        elif PATH_LENGTH > 0 and href[0: PATH_LENGTH] == PATH:
          ''' this is a relative url that lives under our target site '''
          links.append(DOMAIN + href)
        # else:
        #   print(href)
    return links


if __name__ == "__main__":
    process_next()
    import sys
    sys.exit(0)