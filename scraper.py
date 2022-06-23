# scraper for lyrics of stay by zed from metrolyrics.com

import requests
import bs4

def get_all_links(frm):
    retlinks = []
    page_text = requests.get(frm).content
    soup = bs4.BeautifulSoup(page_text,features="lxml")
    links = soup.find_all("a",{"class":"button"})

    for i in links:
        retlinks.append(i['href'])

    return retlinks


def main():
    for i in get_all_links("https://metrolyrics.pro/lyrics/zedd-alessia-cara/stay-lyrics-nyuj8sbi.html"):
        print(i)


main()
