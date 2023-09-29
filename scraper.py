#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

''' this is the website we will scrape '''
URL = "https://avatar.fandom.com/wiki/"



def download(url):
    print(f"fetching '{url}'")
    try: 
      r = requests.get(url)
      page_links = get_links(r.text)
      for link in page_links: 
        print(f"{url} links to {link}")
    except requests.ConnectionError as ce:
      print(f"could not fetch '{url}'", ce)

    
'''
Here's the new method that takes the HTML and finds all the links
'''
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
      href = link.get('href')
      links.append(href)
    return links



if __name__ == "__main__":
    download(URL)
    import sys
    sys.exit(0)