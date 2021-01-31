import time, re
from bs4 import BeautifulSoup
from requests import get as get_web_data
from random import choice as rand_choice
from random import sample, randint
from time import sleep
from os import system

LOCATION_VETO = """ocean
sea
find local businesses
antarctica""".split("\n")

LOCATION_PREFER_NOT = "republic".split("\n")


MAPS_URL = "https://www.google.com/maps/place/{}%C2%B000'00.0%22{}+{}%C2%B000'00.0%22{}?hl=en"
YT_URL = "https://www.youtube.com/results?search_query={}"
DISCOGS_URL = "https://www.discogs.com/search/?q={}&type=release"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Home-a_isNearby.true-a_latitude.20__2E__7466126-a_longitude.40__2E__52837"


def get_random_place():
    longitude = randint(-180, 180)
    latitude = randint(-90, 90)
    place = MAPS_URL.format(abs(latitude),"N" if latitude >= 0 else "S", abs(longitude),  "E" if longitude >= 0 else "W")

    html = get_web_data(place).content

    s = BeautifulSoup(html, features="html.parser")

    img_link = s.find_all("meta", itemprop="image")[0]["content"]
    place_name = s.find_all("meta", property="og:description")[0]["content"]
    place_name = "".join([i for i in "".join(place_name.split(",")[:2]) if not i.isdigit()])

    for veto in LOCATION_VETO:

        if veto in place_name.lower():
            print("VETO", place)
            sleep(5)
            return get_random_place()


    for veto in LOCATION_PREFER_NOT:
        if veto in place_name.lower() and randint(0, 3):
            print("VETO", place)
            sleep(5)
            return get_random_place()


    return latitude, longitude, place_name, img_link


TRIPADVISOR_URL = "https://www.tripadvisor.com/Home-a_isNearby.true-a_latitude.{}__2E__7466126-a_longitude.{}__2E__52837"


def get_new_location():
    return randint(0, 90), randint(0, 180)


def go_random_tripadvisor(url=None):
    if url is None:
        lat, long = get_new_location()
        url = TRIPADVISOR_URL.format(lat, long)

    data = get_web_data(url).content
    soup = BeautifulSoup(data)

    try:
        pois = soup.find_all("a", class_="poi_name")
        poi = rand_choice(pois)

    except Exception as e:
        print(e)
        print(soup)
        print("Nothing found at latitude {}, longitude {}".format(lat, long))
        sleep(randint(2, 7))
        print("Trying again...")
        return go_random_tripadvisor()

    page_url = "http://tripadvisor.com" + poi["href"]

    if "/Tourism" in page_url:

        place = poi.find_all("span")[0].text
        #print("OK let's go to", place)


        return go_random_tripadvisor(page_url)

    elif "/Restaurant" in page_url:

        restaurant = poi.find_all("span")[0].text
        type_ = "restaurant"
        #print("Settled then. We'll eat at", restaurant)
        restaurant = True

    elif "/Attraction" in page_url:

        attraction = poi.find_all("span")[0].text
        type_="attraction"
        #print("I guess we weren't hungry and instead we went to", attraction)

    elif "/Hotel" in page_url:

        hotel = poi.find_all("span")[0].text
        type_="hotel"
        #print("I guess we weren't hungry and instead we went to", attraction)

    else:
        print(page_url)
        print("What should I do?")

    venue_photos_url = page_url + "#photos;aggregationId=&albumid=101&filter=7"

    print(venue_photos_url)

    venue, locale = page_url[page_url.index("Reviews-") + 8:page_url.index(".html")].replace("_", " ").split("-")

    #print("Had a great time at", venue, "in", locale)

    photos_page_html = BeautifulSoup(get_web_data(venue_photos_url).content,
                                     features="html.parser")


    photos = [p for p in photos_page_html.find_all("meta") if p.get("content") is not None and "photo-s" in p["content"]]

    if not photos:
        photos = [p for p in photos_page_html.find_all("img") if p.get("src") is not None and ("photo-l" in p["src"] or "photo-f" in ["src"])]
        elem = "src"
    else:
        elem = "content"


        if len(photos) == 0:
            return go_random_tripadvisor()


    pic = rand_choice(photos)[elem]


    for suffix in "lf":
        if "photo-{}".format(suffix) in pic:
            if get_web_data(pic.replace("photo-{}".format(suffix), "photo-s")).status_code == 200:
                pic = pic.replace("photo-{}".format(suffix), "photo-s")
                break

    print("Here's the pic: ", pic)

    return pic, venue, locale, type_




def get_song(kw=None):


    if kw is None:

        with open("nouns.txt") as f:
            nouns = [line.strip() for line in f]
        with open("verbs.txt") as f:
            verbs = [line.strip() for line in f]

        if randint(0, 2):
            kw = sample(nouns, randint(1, 3))
        else:
            kw = sample(nouns + verbs, randint(1, 3))



    url = DISCOGS_URL.format("+".join(kw))

    #print(url)

    response = get_web_data(url)

    s = BeautifulSoup(response.content, features="html.parser")
    try:
        x = s.find_all("div", class_="card_large")[0]
    except IndexError:
        if len(kw) != 1:
            kw.pop(randint(0, len(kw)-1))
        else:
            kw = None
        get_song(kw)

    pic = x.find_all("a")[0].find_all("span", class_="thumbnail_center")[0].img['data-src']

    song = x.find_all("h4")[0].find_all("a")[0]['title']
    artist = x.find_all("h5")[0].text.strip()

    song_title = "{} - {}".format(artist, song)

    literal = "%22"

    for i in range(2):
        try:
            search_kw = literal + "+".join([w for w in song.split(" ")]) + literal + "+" + literal + "+".join([w for w in artist.split(" ")]) + literal
            youtube_url = YT_URL.format(search_kw)
            print(youtube_url)
            
            x = get_web_data(youtube_url).content
            soup = BeautifulSoup(x, features="html.parser") 
           
            vid_id = soup.find_all("a", class_="yt-simple-endpoint")[0]['href']
            final = "https://www.youtube.com" + vid_id
            break
        except IndexError as e:
            print(e)
            literal = ""
    #
    # GOOG_URL = "https://www.google.com/search?tbm=isch&q={}"
    # url = GOOG_URL.format(search_kw)
    #
    # source = get_web_data(url).content
    # pic = [s['src'] for s in BeautifulSoup(source, features="html.parser").findAll('img') if s.get('src') is not None][2]



    return {"artist":artist,
            "song":song,
            "youtube":final,
            "img":pic,
            "kw":kw}



CHROME = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"'

# non random approach
bands = ['Aphex Twin', '253 scrobbles', 'Geiom', 'Cake', 'Howards Alias', 'Lamb', 'Braintax', 'This Town Needs Guns', 'Augustus Pablo', 'Laura Marling', 'Jurassic 5', 'Reuben', 'Rudi Zygadlo', 'Arctic Monkeys', 'Cashmere Cat', 'Colour', 'Zero 7', 'ClayPigeon', 'Dorian Concept', 'Norah Jones', 'Million Dead', 'Tune-Yards', 'Hudson Mohawke', 'Portishead', 'Luke Vibert', 'Morcheeba', 'Venetian Snares', 'Roots Manuva', 'Boss Kite', 'Mystro', 'DJ Vadim', 'Squarepusher', 'Biffy Clyro', 'Wisp', "Mik Artistik's Ego-Trip", 'St Germain', 'Wagon Christ', '4hero', 'Alice Russell', 'Joni Mitchell', 'Cornershop', 'Nicolas Jaar', 'Maribou State', 'Steely Dan', 'The xx', 'Eels', 'Dr Syntax', 'Sebastian Sturm & Exile Airline', 'Tricky', 'Xincbox', 'Lee "Scratch" Perry & The Upsetters', '146 scrobbles', 'Sonic Boom Six', 'Dismemberment Plan', 'China Shop Bull', 'Roots Manuva Meets Wrongtom', 'Totally Enormous Extinct Dinosaurs', 'Sia', 'Hikes', 'Oscar Jerome', 'Skindred', 'The Streets', 'bitmuch', 'Monobody', "Mo'Kalamity & The Wizards", 'Submotion Orchestra', 'Patrick Wolf', 'The Postal Service', 'John Martyn', 'Stateless', 'Frederic Robinson', 'Gideon Conn', 'Proc Fiskal', 'submerse', 'Andreya Triana', 'Arkist', 'Foals', 'Radiohead', 'Jets to Brazil', 'Semisonic', 'Mount Kimbie', 'Fybe:One', 'Motion City Soundtrack', 'Soom T', 'Asian Dub Foundation', 'Hackman', 'Netsky', 'Hundred Reasons', 'Max Romeo', 'Loyle Carner', 'ArtOfficial',  'Eyedea & Abilities', "Gentleman's Dub Club", 'Resonators', 'Finley Quaye', 'Dizraeli and the Small Gods', 'Romare', 'Imogen Heap', 'Flight of the Conchords', 'Hilltop Hoods', 'Regina Spektor', '1,359 scrobbles', 'Boxcutter', '1,027', 'Nightmares on Wax', 'Prefuse 73', 'Sebastian Sturm', 'Brother Ali', 'Frivolous', 'Bonobo', 'Global Goon', 'Soul Coughing', 'Jamiroquai', "Fat Freddy's Drop", 'Groundation', 'Sublime', 'Björk', 'CHON', 'Thundercat', 'Bear vs. Shark', 'Little Dragon', 'Atmosphere', 'The Skints', 'Baby Mammoth', 'Burial', 'Dizraeli', 'Incubus', 'Belleruche', 'Slugabed', 'Bedouin Soundclash', 'Diane Cluck', 'Babar Luck', 'Khruangbin', 'James Blake', 'Mr. Scruff', 'King Tubby', 'The Flashbulb', 'Jordan Rakei', 'Alborosie', 'System of a Down', 'Scientist', 'Floating Points', 'Capdown', 'Hot Chip', 'Martina Topley Bird', 'RX Bandits', 'Minus the Bear', 'King Prawn', 'Plaid', 'Débruit', 'Elephant Gym', 'Four Tet']

terms = '''official
live
band
song
famous
new album
live in london'''.split('\n')


if __name__ == "__main__":
    
    x = get_song(rand_choice(bands)+ " " + rand_choice(terms))

    system(CHROME + " " + x["youtube"])
