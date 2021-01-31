from json import loads, dumps
from os import getcwd, path, rename
from bs4 import BeautifulSoup
from requests import get as get_web_data
from random import randint, sample
from random import choice as rand_choice
from get_hipster_recommendation import get_song, get_random_place, go_random_tripadvisor
from captions import get_random_song_caption, get_random_thought, get_random_travel_caption, get_random_tripadvisor_caption
from time import sleep
from difflib import SequenceMatcher

USERNAME = "av0cav0cad0sunset"
PASSWORD = "c0linmcr43"
HOURS_PER_POST = 0.5
TOO_SIMILAR = 0.5


#TO DO
# 1. don't say the same things. use files to manage this
# 2. time of day related messages. Morning etc.
# 3. location based posts
# 4. don't post same pics
# 5. like for likes implementation

def similarity(x, y):

    same = SequenceMatcher(None, x, y).ratio()

    return same

def jpeg_props(data):
    data = bytes(list(data))
    off = 0
    while off < len(data):
        while data[off]==0xff:
            off += 1

        mrkr = data[off]
        off += 1

        if(mrkr==0xd8): continue
        if(mrkr==0xd9): break
        if(0xd0<=mrkr and mrkr<=0xd7): continue
        if(mrkr==0x01): continue

        length = (data[off]<<8) or data[off+1]
        off += 2

        if(mrkr==0xc0):
            return {'bpc' : data[off],
            'w'   : (data[off+1]<<8) or data[off+2],
            'h'   : (data[off+3]<<8) or data[off+4],
            'cps' : data[off+5]}

        off += length - 2
    raise Exception("Could not find length")

def contains_html(word):
    for token in [">", "<", "/", "http"]:
        if token in word:
            return True

    return all([c.isdigit() for c in word])  or any([ord(c) > 128 for c in word] or all([not i.isalpha() for i in word]))


def subarray_match(array1, array2, start_point=0):

    if len(array2) > len(array1):
        raise Exception("array 2 cannot be bigger")
    i = start_point
    found = False
    while i < len(array1) and not found:
        word = array1[i]
        print("Word is", word)
        if word == array2[0]:
            print("Matches")
            found = True
            for w1, w2 in zip(array1[i:], array2):
                print("Comp", w1, w2)
                if w2 not in w1:
                    found = False
                    break

            if found:
                return i
        i += 1
    if not found:
        raise Exception("Sub string not found")

def random_pic():

    id_ = randint(1, 500)
    url = "https://i.picsum.photos/id/{}/400/400.jpg".format(id_)
    img = get_web_data(url).content
    print(url)
    return img


def search_for_text(words):
    words = words.lower()

    search = "+".join([w for w in words.split(" ")])
    url = "https://www.google.com/search?&q=%22{0}%22&oq=%22{0}%22".format(search)
    data = get_web_data(url).content
    soup = BeautifulSoup(data, features="html.parser")
    text = soup.text.lower()
    print(text)
    occurrences = text.count(words)

    words = words.split(" ")
    extract = text.split(" ")
    print(extract)
    print(words)
    pos = subarray_match(extract, words, start_point=randint(0, len(extract) - 20))
    step = rand_choice([-1, 1])
    print("pos is", pos)
    if step == -1:
        end = 0
    else:
        pos = pos + len(words)
        end = len(extract) - 1
    out = list(words)

    i = pos
    stop = False
    while i != end and not stop:
        word = extract[i]
        print(word)
        for token in SENTENCE_END:
            if token in word or contains_html(word):
                print("Encountered illegal token", word)
                stop = True
                break
        if not stop:
            if step == 1:
                out.append(word)
            else:
                out.insert(0, word)
        i += step


    return out

def find_new_friends(number, topics):
    pass


def post_image(bot, caption, img, fn=None, latitude=0, longitude=0):
    options = {}

    w = caption.split(" ")
    if fn == "":
        fn = "_".join(w[1:randint(3, 6)]).replace("#", "")+".jpg"
    full_path = getcwd() + "/" + fn
    i = 1
    while path.exists(full_path):
        print(fn)
        fn = fn.replace(".jpg", "({}).jpg".format(i))
        i += 1
        full_path = getcwd() + "/" + fn


    with open(fn, "wb") as f:
        f.write(img)

    id_ = [str(int(i)+randint(1, 10))[0] for i in str(796049897513062)]

    if latitude != 0 and longitude != 0:
        options["location"] = {"lat":latitude, "lng":longitude}



    bot.upload_photo(full_path, caption=caption)



def album_cover_challenge(day):
    try:
        import instabot
        bot = instabot.Bot()
        bot.login(username=USERNAME, password=PASSWORD, proxy=None)

        song_data = get_song()
        song, artist = song_data['song'], song_data['artist']
        text = "".join([t for t in artist + song if t.isalpha()])
        fn = "{}.jpg".format(text)
        img = get_web_data(song_data['img']).content
        youtube = song_data["youtube"]
        caption = """DAY {}
        
        I've been given a task to choose ten albums that greatly influenced my taste in music. One album per day for ten consecutive days. No explanations, no reviews, just album covers.""".format(day)
        post_image(bot, caption, img, fn)
        bot.logout()
        return True
    except:
        return False


def place_or_music_or_thought():
    import instabot
    bot = instabot.Bot()
    bot.login(username=USERNAME, password=PASSWORD, proxy=None)

    latitude, longitude = 0, 0



    if 0: #not randint(0, 3):
        pic, venue, locale, type_ = go_random_tripadvisor()
        caption = get_random_tripadvisor_caption(venue, locale, type_)
        fn = "{}.jpg".format(randint(1111, 9999))
        img = get_web_data(pic).content


    elif randint(0, 1): #need to fix randint(0, 2):

        latitude, longitude, place_name, img = get_random_place()
        img = get_web_data(img).content
        caption = get_random_travel_caption(place_name)
        text = "".join([t for t in place_name if t.isalpha()])
        fn = "{}.jpg".format(text)

    elif randint(0, 1):

        song_data = get_song()
        song, artist = song_data['song'], song_data['artist']
        text = "".join([t for t in artist + song if t.isalpha()])
        fn = "{}.jpg".format(text)
        img = get_web_data(song_data['img']).content
        youtube = song_data["youtube"]
        caption = get_random_song_caption(song, artist, youtube)


    else:

        caption = get_random_thought()
        img = random_pic()
        fn = ""
    try:
        with open("previous_captions.json", "r", encoding="utf-8") as f:
            previous_captions = loads(f.read())

        for cap in previous_captions:
            if similarity(cap, caption) >= TOO_SIMILAR:
                print(cap)
                print("...and...")
                print(caption)
                print("... deemed too similar")
                place_or_music_or_thought()

        previous_captions.append(caption)

    except:
        previous_captions = [caption]

    post_image(bot, caption, img, fn, latitude, longitude)
    with open("previous_captions.json", "w", encoding="utf-8") as f:
        f.write(dumps(previous_captions))

    bot.logout()

def del_cookie():
    i = 0
    pathy = getcwd() + "/ config/av0cav0cad0sunset_uuid_and_cookie{}.json".format(i)
    while path.exists(pathy):
        i += 1
        pathy = getcwd() + "/config/av0cav0cad0sunset_uuid_and_cookie{}.json".format(i)
    try:
        rename(getcwd() + "/config/av0cav0cad0sunset_uuid_and_cookie.json", pathy)
        print("deleted the cookie")
    except:
        pass

if __name__ == "__main__":



    while True:
        try:
            del_cookie()
            place_or_music_or_thought()
            sleep(int(60 * HOURS_PER_POST * randint(45, 69)))
        except Exception as e:

            print(e)
            sleep(randint(10, 30))












