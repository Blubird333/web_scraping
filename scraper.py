# scraper for lyrics of stay by zed from metrolyrics.com

import requests
import bs4

lyrics= requests.get("https://metrolyrics.pro/lyrics/zedd-alessia-cara/stay-lyrics-nyuj8sbi.html").content

soup = bs4.BeautifulSoup(lyrics,features="lxml")

all_a_tags = soup.find_all("a",{"class":"button"})

#all 'a' tags in with the class 'button'.
for i in all_a_tags:
    print(i)
print("**********************************************************************************************************")

#links for all 'a' tags with the class 'button'
for i in all_a_tags:
    print(i['href'])
