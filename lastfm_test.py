


YT_URL = "https://www.youtube.com/results?search_query={}"
DISCOGS_URL = "https://www.discogs.com/search/?q={}&type=release"

import time, re
from bs4 import BeautifulSoup
from requests import get as get_web_data
from random import choice as rand_choice
from random import sample, randint

with open("nouns.txt") as f:
    nouns = [line.strip() for line in f]

kw = sample(nouns, randint(1, 4))

print(kw)

url = DISCOGS_URL.format("+".join(kw))

#print(url)

response = get_web_data(url)

s = BeautifulSoup(response.content, features="html.parser")

x = s.find_all("div", class_="card_large")[0]
img = x.find_all("a")[0].find_all("span", class_="thumbnail_center")[0].img['data-src']
input(img)
song = x.find_all("h4")[0].find_all("a")[0]['title']
artist = x.find_all("h5")[0].text.strip()

song_title = "{} - {}".format(artist, song)

search_kw = "+".join([w for w in song_title.split(" ")])

youtube_url = YT_URL.format(search_kw)

soup = BeautifulSoup(get_web_data(youtube_url).content, features="html.parser")

vid_id = soup.find_all("a", class_="yt-uix-tile-link")[0]['href']

final = "https://www.youtube.com" + vid_id

GOOG_URL = "https://www.google.com/search?tbm=isch&q={}"

url = GOOG_URL.format(search_kw)

source = get_web_data(url).content
pic = [s['src'] for s in BeautifulSoup(source, features="html.parser").findAll('img') if s.get('src') is not None][2]

