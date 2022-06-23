# attempting to get the lyrics from the webpage "https://metrolyrics.pro/lyrics/zedd-alessia-cara/stay-lyrics-nyuj8sbi.html"

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

def main():
    for i in get_all_links("https://metrolyrics.pro"):
        print(i)

main()
