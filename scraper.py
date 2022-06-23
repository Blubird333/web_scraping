# scraper for lyrics of stay by zed from metrolyrics.com

import requests

lyrics= requests.get("https://metrolyrics.pro/lyrics/zedd-alessia-cara/stay-lyrics-nyuj8sbi.html").content

print(lyrics)
