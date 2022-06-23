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
