#!/usr/bin/env python3

import requests

''' this is the website we will scrape '''
URL = "https://avatar.fandom.com/wiki/"


'''
This is the method that does the work of going out to the internet
and downloading the page. 
'''
def download(url):
    print(f"fetching '{url}'")
    try: 
      r = requests.get(url)
      '''
      What does the html look like?
      '''
      print(r.text)
    except requests.ConnectionError as ce:
      print(f"could not fetch '{url}'", ce)
    

'''
this line
  if __name__ == "__main__":
allows you to parse arguments that are passed in from the CLI. 
We don't need that here, but it's not a bad habit to get into. 
'''
if __name__ == "__main__":
    download(URL)
    import sys
    sys.exit(0)