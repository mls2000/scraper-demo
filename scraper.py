#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


''' this is the website we will scrape '''
URL = "https://avatar.fandom.com/wiki/"
''' 
While parsing links on the site, we will need to handle both 
absolute (http://site/subfolder) and relative (/subfolder/) links. 

And when we convert the path into a filename, it will be handy to 
know the length of the url as a string, in order to quickly remove
it from the file path
'''
URL_LENGTH = len(URL)
''' grab the various parts of the url '''
PARSED = urlparse(URL)
DOMAIN = f"{PARSED.scheme}://{PARSED.netloc}"
PATH = PARSED.path
PATH_LENGTH = len(PATH) if len(PATH.replace('/', '')) > 0 else 0



def download(url):
    print(f"fetching '{url}'")
    try: 
      r = requests.get(url)
      page_links = get_links(r.text, url)
      for link in page_links: 
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
    download(URL)
    import sys
    sys.exit(0)