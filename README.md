# Let's build a scraper

Sometimes you can get your data by downloading a zipped up file. And sometimes, you need to visit every single page on a website and copy it. In the latter case, we call this a scraper, and this code base shows how to make a simple one. 

## Parse the pages

Up to this point, our code has fetched all the pages from a remote website and made local copies. But we haven't tried to extract anything interesting from the pages we copied. This is intentional! For many real world data scraping tasks, you don't know what you want at the start, or how to find it. Making a local copy lets you poke around without having to scrape the site every time you get a new idea. Once you do know how to find what you're after, then it can be a good idea to extract the good stuff as soon as you fetch it. But we aren't there yet.

If you take one of the pages we downloaded and open it in a browser, it does not look like what's on the original site. There are huge icons, there's no header row for navigation, the colors are brutal, etc. A modern web page can have lots of extra files to make it look and act like it does, and we haven't fetched those. This reveals just how much boilerplate stuff is on the page; for the example page I pulled up, the interesting stuff doesn't show up until 80% of the way down. 

Once you find the stuff you want, you can try to figure out how to extract it from the page. If you right click in the browser, most modern browsers have an "Inspect" or "Inspect Element" option. This will open up a new panel that lets you see into the web page source code. The cool thing is that moving your mouse over something in this panel will highlight that item in the web page. The thing you started with might be a little too specific, but it will often be nested inside other elements–that's indicated by the indentation. Moving your mouse around in the inspector panel, you can zoom out until you find the element you want. Then you can check if it has an `id` or `class` that you can use to identify it. In this example, the pages have a title with a class of `page-header__title-wrapper`, and the other interesting stuff is in a `div` element with an id of `content`. 

Note that the information under content can take a lot of different shapes: some pages discuss people, some places, etc., and what's important about them changes. Further work could try to find what's interesting about places and extract that, and same for people. This example isn't going that deep, because that will change very much for different websites. 

We use the BeautifulSoup library to find all the links on a page in our `get_links` method. The method we used was `find_all`, and it lets us find all the elements of a certain type (we looked for `<a>` tags). There's another method called `select`, and a variant called `select_one`, that allows for searching by id, or class, or tag type (if you're into front end web development, it uses CSS selectors). Since we know the id and class name of the elements we are after, this is a natural fit here.


In order to evaluate all the files we download, we use python's built in methods to traverse all the files in a directory. For each one, we pull the title and the key content using beautiful soup, and then save them in a new file in the `parsed` folder. 





## fin

enter 
'''
git checkout main
''' 
to jump to the final working code. To see all the steps, you can do
'''
git branch
'''


