# Let's build a scraper

Sometimes you can get your data by downloading a zipped up file. And sometimes, you need to visit every single page on a website and copy it. In the latter case, we call this a scraper, and this code base shows how to make a simple one. 

## Save the results

So we know we can find all the links, but it doesn't do a lot of good if we don't save the results. In this step, we'll make a folder called `scraped` and save the downloaded pages in a directory structure that echos the site we are scraping.

We'll import python's built in `os` and `os.path` libraries to navigate and create directories as needed. 

Note the most complexity in this step is turning url into a filename. We isolate that logic in a new method `get_filepath_from_url`. 

Note that we add the `scraped` folder to the `.gitignore` file. That will prevent us from checking the results of the scraping into git. That often makes sense: this could end up being more data than our git repo has room for, and might change so often that we don't want to save every iteration of the data. 

And tada! We have a scraper that copies our target website. But we haven't extracted any useful information from the those webpages yet. That's what we will do next. 



## next

enter 
'''
git checkout step006
''' 
to see the next step. Or, if you want to jump to the final working code, go to 
'''
git checkout final
'''
To see all the steps, you can do
'''
git branch
'''


