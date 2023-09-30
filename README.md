# Let's build a scraper

Sometimes you can get your data by downloading a zipped up file. And sometimes, you need to visit every single page on a website and copy it. In the latter case, we call this a scraper, and this code base shows how to make a simple one. 

## Start fetching more pages

So far we built something that finds all the links we want on one and only one page. Our next step is to then visit all those links. 

One thing we want to prevent is visiting the same page twice. Imagine your second page links back to the first. You store the link to the first page, then visit it again and get the link to the second. Then back to the first, and so on, and so on. It seems obvious, but it's an easy mistake to make. We'll save a set of all the links we find so that we only go to each one once. We will also have a list of the links we need to visit, and we'll remove items from that as we visit them. 

Also, as we get further into the site, some more pages come up that we can probably skip. There are some that end in "?edit": we don't want our scraper to edit pages. Let's add something to prevent that. In fact, any time there's a question mark in the url, that's an indication that the server is doing some sort of special variation on the page. For this site, it's unlikely we are interested in that, so remove anything after the "?".

Another consideration is that some servers can't handle a flood of requests. It can be useful for both you and the server administrators if you add a little wait time between requests. We'll use the `sleep` method from python's `time` library for this. 

Lastly, we will make another method that checks whether any more pages need to be fetched, and then calls our download method as needed. 


## next

enter 
```
git checkout step005
``` 
to see the next step. Or, if you want to jump to the final working code, go to 
```
git checkout main
```
To see all the steps, you can do
```
git branch
```

