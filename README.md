# Scraping

## Getting the virtual environment setup
1. Install 'virtualenv'. You can install vurtualenv tool using
   'sudo apt-get install python3-virtualenv' (on Ubuntu)

2. Create a virtual environment using 'virtualenv -p /usr/bin/python3 /tmp/mscraper'.
   You can change the location of you virtualenv. I've used '/tmp/mscraper' as an example.

3. Then activate the virtualenv using '. /tmp/mscraper/bin/activate'.
   You can deactivate it by typing 'deactivate' and hitting enter.

## Installing packages
1. After activating your virtualenv, use 'pip install requests' to install the requests library.

2. Install BeautifulSoup library using 'pip install beautifusoup4'.

## Getting the info from the webpage
Look into scraper.py (with previous commits)

##### Inside the scraper.py
This is the file that can be used to download the lyrics of more than one song from a particular website.Steps are as follows:

 - import bs4 and requests
 - First make a method called 'get_all_links' which should function to return all the similar links that we are going to access.
 - Then make another method called 'get_lyrics' which should function to return the lyrics of the song in that particular website.
 - Note that all the links from get_all_links method should have same structure.(generally, in any website the structure is same.)
 - make another method called 'get_filename' to change the .html to .txt[so that the downloaded content is in .txt format]
 - make a 'main' method to unify all the defined methods and download the contents of the website.Using the code lines:-
 - read the 'scraper.py' for further details.
