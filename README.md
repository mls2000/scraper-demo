# Let's build a scraper

Sometimes you can get your data by downloading a zipped up file. And sometimes, you need to visit every single page on a website and copy it. In the latter case, we call this a scraper, and this code base shows how to make a simple one. 

## parse the document for links

To make a useful scraper, you need to find the links in the document, and save them to direct your scraper to visit them too. In this step, we introduce the BeautifulSoup library for traversing html. We use that in the new method we create to look for all the anchor tags `<a>` in a page and get the links from them. We don't go and fetch the next page yet. Instead, let's take a second to look at the links we are getting. 


If you run this, you'll see a lot of links look like `/wiki/Appa` or `/wiki/Toph_Beifong`. That's not a url that will work by itself: instead, it's relative to the page it's being called from. We'll have to handle those relative urls for our scraper to work. 

Also, there's a link to `http://www.amazon.com/dp/B000FZETI4`. We don't want to fetch outside our site, and we definitely don't want to start scraping the entire amazon site–it'll go on forever. So if it's not a relative url, we'll want to make sure that the beginning of the url starts with our target site. 

There is also a link to `#`. That's just a different location on the same page: we can skip anything that starts with `#`. 

We'll handle all of those cases next. 


## next

enter 
'''
git checkout step003
''' 
to see the next step. Or, if you want to jump to the final working code, go to 
'''
git checkout final
'''
To see all the steps, you can do
'''
git tag
'''


