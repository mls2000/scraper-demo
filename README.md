# Let's build a scraper

Sometimes you can get your data by downloading a zipped up file. And sometimes, you need to visit every single page on a website and copy it. In the latter case, we call this a scraper, and this code base shows how to make a simple one. 

## handle all the variations of link types. 

In addition to relative and absolute links, some links start with `//` instead of `http://` or `https://`. There can be more complexity around relative links as well: are they from a url that ends with '.html' or not? Here the `` method is built out to handle these cases. We take advantage of python's built in urllib library to parse the URL into different parts. We can use those to compare the incoming link to our target, and to build out an absolute link that we can pass into the download method.  


## next

enter 
'''
git checkout step004
''' 
to see the next step. Or, if you want to jump to the final working code, go to 
'''
git checkout final
'''
To see all the steps, you can do
'''
git tag
'''


