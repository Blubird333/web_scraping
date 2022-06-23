# scraper for lyrics of stay by zed from metrolyrics.com
# scraper means to copy obtain the information contained in the websites.

import requests
import bs4

def get_all_links(url):
    retlinks = []
    page_text = requests.get(url).content
    soup = bs4.BeautifulSoup(page_text,features = 'html.parser')
    links = soup.find_all("a",{"class":"thumb pull-left _trackLink"})

    for i in links:
        retlinks.append(i['href'])

    return retlinks


def get_lyrics(url):
    ret_ly=[]
    page_text = requests.get(url).content
    soup = bs4.BeautifulSoup(page_text,features = 'html.parser')
    ly_tag = soup.find_all("p",{"class":"_lyricContent"})

    all_txt = soup.get_text(" ",strip=True)

    for i in ly_tag:
        ret_ly.append(i.get_text())

    return "\n".join(ret_ly)


def get_filename(url):
    return url.split("/")[-1].replace("html","txt")


def main():
    for i in get_all_links("https://metrolyrics.pro"):
        print(f"Downloading {i}")
        lyrics = get_lyrics(i)
        fname = get_filename(i)
        with open(fname,"w") as f:
            f.write(lyrics)


main()
