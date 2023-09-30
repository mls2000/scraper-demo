# Let's build a scraper

Sometimes you can get your data by downloading a zipped up file. And sometimes, you need to visit every single page on a website and copy it. In the latter case, we call this a scraper, and this code base shows how to make a simple one. 


## Requirements: 
We're going to assume some basic knowledge of working with a command line interface (CLI). You'll need git and python installed. Python is a programming language that is both powerful and easy to read (at least as far as programming languages go). Git is a tool for version control: it lets you jump back and forth between different versions of your code. When you download this code base, you get the completed example. But if you want to learn how it gets built up, we use git for that. 

#### Mac
Python3 comes installed on most macs these days. You can test whether you have python3 by opening up a window in the Terminal app and running 
```
which python3
```
If the line after that should show an absolute path that ends with "/python3". If you just get another prompt, then it's not installed. Similarly, you can check for git by running 
```
which git
```

This page has notes on installing git: 
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
And the instructions on this page can help you get python installed. 
https://www.python.org/downloads/

And if by chance you have homebrew installed, the brew installation of python is perfectly fine. And if you don't know what that is, ignore this. 


#### Windows
I have less experience here, but you may want to install python from the Microsoft store. There's a tutorial here on 
getting started with python
https://learn.microsoft.com/en-us/windows/python/beginners

and this page will get you started with git. 
https://git-scm.com/download/win



## To install

use git to download this repository: 
```
git clone https://github.com/mschifferli/jcml-scraper-demo.git
```
this will make a new folder named "jcml-scraper-demo". `cd` into that. 

#### making a sandbox with `venv`

We will need to install some libraries to get this running, and we will use a python `virtualenv` to manage them. If you haven't used this before, it's a sandbox where we can install any library we want without having to worry about whether it will conflict with libraries required for other projects. There are two steps: 1) creating the sandbox and 2) activating the sandbox. 

Creating the sandbox is a one time thing. Run this command:
```
python3 -m venv venv
```
This creates a folder called `venv` to store the libraries you want to install. But first you have to activate it: run 
```
source venv/bin/activate
```
You'll need to do this every time you open a new CLI prompt. You can tell it's active because by default it updates your CLI prompt to have a `(venv) ` at the front of it. 

#### installing the requirements

With the virtual environment ready, we can now run
```
pip install -r requirements.txt
```
Which will download the two libraries we need, `requests` and `beautifulsoup4`. 


## To run

The first step is simple: can we get python to fetch a web page? There isn't much code here, but after getting through the chores of setting up a project (building the venv, getting your imports, setting up the script to be callable, etc.), it's nice to give yourself a little reward and see that everything is working as it should. 


## next

enter 
'''
git checkout step002
''' 
to see the next step. Or, if you want to jump to the final working code, go to 
'''
git checkout main
'''
To see all the steps, you can do
'''
git branch
'''


