from random import choice as rand_choice
from random import sample, randint


# 0 pronoun
# 1 verb
# 2 possessive
# 3 noun

with open("nouns.txt") as f:
    NOUNS = [i.strip() for i in f.readlines()]
with open("verbs.txt") as f:
    VERBS = [i.strip() for i in f.readlines()]
with open("pronouns.txt") as f:
    PRONOUNS = [i.strip() for i in f.readlines()]
with open("possessives.txt") as f:
    POSSESSIVES = [i.strip() for i in f.readlines()]
with open("tags.txt", encoding="utf-8") as f:
    TAGS = [i.strip() for i in f.readlines()]
with open("emojis.txt", encoding="utf-8") as f:
    EMOJIS = [i.strip() for i in f.readlines()]
with open("common.txt", encoding="utf-8") as f:
    COMMON = [i.strip() for i in f.readlines()]
with open("past_verbs.txt") as f:
    PAST_VERBS = [i.strip() for i in f.readlines()]
with open("adjectives.txt") as f:
    ADJECTIVES = [i.strip() for i in f.readlines()]
with open("foods.txt") as f:
    FOODS = [i.strip() for i in f.readlines()]

num = randint(111, 999)


SONG_CAPTIONS = ("""Have you heard these ABSOLUTE VIBEZ? {1} - {0}
Been really feelin' {0} by {1} lately.
Been really diggin' {0} by {1} today - so live!
Been dancin' around all day like a madman to {0} by {1} LOLLL!
Omg I must have listened to "{0}" by {1} about """ + str(num) + """ times today!!!
Song of the week: {1} - {0}
Have you heard this WICKED track? {1} - {0}
Nothing like a bit of {1} to get the PARTY started!
"{0}" by {1} got to be one of my all time favourites.
Just love the beat in this track - {1} - {0}
"{0}" by {1}. Real dynamite riddims.
{1} - {0} KILLER SOUND!
{1} - {0} such a sweet melody in this one.
{1} - {0} an all-time classic.
"{0}" by {1}, absolutely timeless.
"{0}" by {1} PLAY THIS AT MY FUNERALLLLLLLLLL!!!!!!!!!!!!!
"{0}" by {1} I could EAT this is sounds so good
{1} have killed it with this one. U heard the bass in their song "{0}"???
Hear the bass, hear the riddim {1} - {0}
I think I know EVERY SINGLE WORD to "{0}".
{0} deserves an OBE for this one - pure aural delights.
{1} have outdone themselves again. {0} is EPIC.
"{0}" is such a groovy song.
{1} - {0} : FUNKY!
It's not often I say this. But I really feel that {1} - {0} is one of those life-changing songs, y'know??
I can't wait to see {1} LIVE IN CONCERT this november!!! Gonna be singing along to every word in "{0}" y'know.. FOR REAL!"
Check out "{0}" by {1}. Stay tuned for my sik beat using this acapella!
Heard the groove in "{0}" by {1}? JUS WAIT for the bars I will spit over this one!
Dum dum chhh dum dum chhhh dum dum chhhh LOVE IT!
All that's missing in {0} is a bit of violin, do you agree?
Can't wait for the reunion. {1}: {1}
When's the new album coming out?? {1}: {1}
This is the song of the century. {1} #megafan.""").split("\n")

optional_freq_adj = """sometimes
never
always
mostly always
continuously
forever

""".split("\n")

adverb = """plausibly
probably
maybe
perhaps
basically
pretty much
likely
arguably
- theoretically speaking -
ideally
desirably

""".split("\n")


THOUGHTS = """I don't know why <0> {0} <1> <2> <3>
<0> is thinking about <2> <3>
Today is just <3> <3> <3>!!!
Are you sure you can <1>?
Are you used to all of this <3>?
As far as <0> knows... it's all just <3>.
As far as <0> is concerned, <3> baby!
Be careful with <2> <3>. {1}, just leave it alone altogether.
But this doesn’t mean that <2> <3> is <1>ed...
By the way, have you seen <2> <3>?
Compared to <2> <3>, I'd {1} like to see more <1>!
Did you used to <1> <3>?
{1}, don’t ever <1> <3>.
Do you agree with <2> <3>?
Do you have any <3> available?
Do you mind if I {1} <1>?
Do you feel like some <3>?
Shouldn’t we <1> <3> now?
Have you ever <5> <3>?
{1} not until <0> <1>s <2> <3>.
He is so <4> that <4> was the only thing <0> could do.
<0> is not only <3> but also <4>...
Help yourself to all of my <3>.
How about <3> <3> and more <3>?
How come <0> {0} wants to <2> the <3>?
How dare <0>! <6>!!
How do you like <2> <3>?
How long does it take to <1> a <3>?
<0> is as <6> as a <3>
He is either <6> or a <3>, you decide.
<0> is so <6> that the only choice is to make <3> <1>.
<0> is not only <6> but also a <3>.
Help yourself to <2> <3>.
How about <6> <3>?
How come <0> <1>?
How dare you! I worked hard for this <6> <3>.
How do you like your <6> <4>?
How long does it take for a <6> <4> to <1> a <6> <3>?
How often does your <6> <4> <1> <6> <3>s?
I bet your <3> {0} likes to <1> <6> <4>.
I can hardly believe that <6> <4> <1> <6> <3>!
I can’t help but <1> <6> <4>.
I can’t say "<6> <3>", but I will...
I cannot wait to <1>. <3> <4> everyone!
I dare say "<1>". Will you <1> with <0>?
<0> would like you to be a bit more <6>…
I’d hate for you to <1> whilst the <6> <4> <1>s at the same time
If it hadn’t <5> we'd be more <6>.
If there is one thing that <1> me, it’s <0>'s <6> <5>.
I have no idea about <1>. Maybe <0> could tell me when they <5>.
I have got to <1> before <6> <4> make an appearance.
As {1} as possible <0> will be here soon.
I’ll let you know when <0> <1> <3>.
I’d be grateful if {0} can {1} today.""".format(rand_choice(optional_freq_adj), rand_choice(adverb)).split("\n")

tbc = """I bet…
I can hardly believe that…
I can’t help…
I can’t say…
I cannot wait to…
I dare say…
I’d like you to…
I’d hate for you to…
If it hadn’t been for…
If there is one thing that… me, it’s…
I have no idea…
I have got to…
 as… as possible
I’ll let you know…
I’d be grateful…
I’m afraid…
I’m calling to…
I’m looking forward to…
I’m not really happy with…
I’m thinking about…
I really go for…
It is… that…
It’s too bad that…
It’s my fault for…
It’s not that… but…
It’s on the tip of my tongue.
It’s said that…
It’s up to…
It’s your turn…
It may surprise you, but…
I have been…
I’ve had enough of…
I wonder if…？
I would rather… than…
No matter what…
No wonder…
Now that I (come to) think about it,…
Once you…
… only to find…
On one hand…on the other hand…
See that…
Speaking of…
Thanks to…
Thank you for…
The first thing I’m going to do when… is…
The more…the more…
There is nothing as…as…
There is nothing I like better than…
We’d be better off without…
We’d better…
We may as well…
What becomes of…？
What can I do for…？
What do you mean by…?
…what-do-you-call-it (what·cha·ma·call·it)
What do you say…?
What… for…
What if…?
What I’m trying to say is…
What’s the matter with…?
What would you do if…?
What’s the use of…?
What’s your favorite…?
Where can I…?
Where there is… there is…
Whether or not…
Why not…?
Would you care for …?
You are not to…
You can never… too…
You only have to…in order to…


""".split("\n")


sights = """mountains
nature
beaches
rivers
animals
seagulls
greenery
scenary
local communities""".split("\n")

adjectives = """massive
beautiful
amazing
brilliant
eye-opening
gorgeous
delightful
crazy
excellent
amazing
humongous
MEGA
rad
bangin'
EPIC
wicked
lovely
cool
legit
great
really amazing
tear-worthy
memorable
life-changing""".split("\n")

activities = """hiking
boating
running
eating out
mountain climbing
beach bumming
sunbathing
partying
shopping
sightseeing
pub crawl
bar crawl
local culture
off the beaten path""".split("\n")

number = str(randint(2, 25))

date = rand_choice("""Jan
Feb
March
April
May
June
July
August
Sep
Oct
Nov
Dec""".split("\n")) + " '" + str(randint(7, 20)).zfill(2)

intros = """YO!
HEY PPL!
LISTEN UP!
WORD UP!
Party people!!!
Culture vultures!!!
BRos!
Peeps!
Good Morning people!
Afternoon!
Evenin' all.
STOP AND THINK:
Silence.
MEMORIES:







""".split("\n")

travel_quotes = """Can't wait to travel to {0}!!!
Do you remember when we hung out in {0}?
Can't wait to go back to {0}.
Next trip after this: {0}!
Saw some {5} {1} in {0}
Got everything packed for my trip to {0}
Just booking tickets to go to {0}!!! Skyscanner, you're the best @SkyScanner
Anyone know what kind of daily budget is needed in {0}? On a shoestring.
Any good {2} suggestions for {0}?
Any good local tips for {0}?
Off to {0} next month. Don't think my suitcase is big enough!!!
SEVEN DAYS IN {0}!!!! {5}: PACKED!
Maybe I'll see the {1} in {0} next year?
Moving to {0} in 2021, wish me luck!!!
{3} days {2} in {0}.. can't wait!
Anyone got a lonely planet for {0} I can borrow???
{2} in {0} - {4}. An absolutely {5} time.
{2} in {0} - {4}. So {5}!.
{2} in {0} - {4}. What a {5} vacation.
{2} in {0} - {4}. What a {5} trip!
{2} in {0} - {4} - next time YOU ARE COMING WITH ME!!!
Not long until {0}. Don't let me forget my {6}.
{5}? Check. Sense of adventure? Check. {0}: here I come!!!
{0} - dreams of yesteryear. {4}
Hope to re-live the highlights of {0} - {4} very soon.
Mum, Dad, when can we go to {0} again?
Thinking of making some videos on the local {2} scene in {0}. Your thoughts?
Thinking of writing a blog about the {5} {2} scene in {0}. You with me?
Might do a skit on the {5} {2} scene in {0}. You game?
Stay tuned for a series on all them peeps in the {2} scene in {0}.
Newsflash: My first book will be on the {5} {2} phenomenon in {0}.
OK guys, listen up. I'm going to to a short piece on the {5} {2} scene in {0}. You ready?!
*raps* Mofo aint ever going back, all the way to {0}.
{5} {0}!!!!! 
Perhaps I'll do some recipes on the cuisine from {0} soon. All you tummies stay tuned!
Today's inspiration: {0} - {4}
The vibe today is definitely {0} - {4}
Memories today: {0} - {4}
Take me back to {4} and {0} NOW!!!!!!!!!
{3} years since my {5} {2} in {0}. Those were the days.
{3} years since my {5} {2} in {0}. Time of my life.
Seriosuly, a LOT of the time people ask me about my time spent {2} in {0}. One word: {5}.
How was the {2} in {0} you ask? {5}.
Who got the {5}? {0} - {4}.""".split("\n")

holiday_equipment = """suncream
sunglasses
binoculars
sunhat
hiking boots
snorkel
snowboard
wanderlust
travel guide
lonely planet
tripadvisor
phrase book
pina colada""".split("\n")


attraction_quotes = """Just got back from {} in {}.
Spent the morning at {} in {}.
A few years back we went to {} in {}.
Yesterday's treat was going to {} in {}.
Managed to get a 2 for 1 voucher for {} in {}.
Got a sweet groupon deal for {} in {}.
What a <adjective> time at {} in {}.
<number> hours one day at {} in {}.
<pronoun> surprised me on that day with a trip to {} in {}
Woke up at <number> AM, straightaway <pronoun> yells GET DRESSED we're off to {}!!! It was my first time in {}, and I thought what a <adjective> experience!
{}, {} this morning. <adjective>! <adjective>!! <adjective>!!!
{}, {}. Thanks for the rec TripAdvisor!
Queue was TOO LONG that day at {} in {}.
Too many ppl on that day at {} in {}.""".replace("<number>", str(randint(2, 7))).replace("<pronoun>", rand_choice(PRONOUNS).capitalize()).replace("<adjective>", rand_choice(adjectives)).split("\n")

more_attraction = """I really liked the vibe of the place.
There was just too many people for my liking.
The decor could be improved...
It would be good if they had a McDonalds.
I even got a T-Shirt!
Why no fridge magnets though?
Next time I will make sure to bring {0}
The cut of their jib was just {1}!
{1} soundtrack, too.
Next time i'll wear my waterproofs.
Next time I'll bring my {0}.
Only issue was I forgot my {0}.
....{1}...  .{0}......""".format(rand_choice(holiday_equipment), rand_choice(adjectives)).split("\n")

closing_comments = """5* would recommend.
10/10!!!
3.5 / 10 stars.
A************
TOP ATTRACTION!
I'll be back!
SEe you again next year!
I will be telling ALL of my friends.
Followers - hear ye!
This is too good to miss.
100% great time.
Next time I'd go with more people.
Next time I'm bringing {0}!
I only wish {0} was there with me.
{0} especially loved the {1}.""".format(rand_choice(PRONOUNS), rand_choice(holiday_equipment)).split("\n")



timeframe = """this week
that morning
a few months ago
last Weds
last Mon
last Tuesday
the other day
a few days ago
last Sunday
last weekend
last month
on Saturday
on Thursday
2 weeks ago Thursday""".split("\n")


restaurant_intros = """<pronoun> always takes me here: {0} ({1}).
{0} ({1}) with <pronoun> <timeframe> - yummy!
{0} ({1}) one word : STUFFED!
{0} ({1}) so absolutely delicious!
{0} ({1}) I was starving, now I'm completely full!
Was in {1} <timeframe> so popped into {0} for a quick bite to eat.
Happened to be in {1} <timeframe> so wandered into {0} by chance.
Was visiting <pronoun> in {1} <timeframe> so went for some lunch at {0}.
It'd been ages since me and <pronoun> spoiled ourselves, so {0} in {1} it was.
If you're ever in {1}, seriously check out {0}!
Me and <pronoun> were v hungry <timeframe>.. luckily {0} was just round the corner.
Cold, hungry and alone in {1}? May I recommend {0}?
If you're up for some <adjective> munch in {1}: {0} is your best bet.
Fancy some <adjective> dinner in {1}? Then get straight down to {0}!
If you're starving and anywhere near {1} then get yourself to {0} - trust me.
Had to undo my belt <timeframe> after eating at {0}.
Aint no decent <food> in {1} ppl say? You clearly aint been to {0}.
Make sure you go to {0} with an appetite. Some of the biggest portions I've seen in the whole of {1}.
{0}, {1}. This is fine dining with a capital F.
{0}. I don't think there's a better joint in the whole of {1}.
My favourite shack for home cooked meals is {0} in {1}.
ON a budget and hungry in {1}? Get straight down to {0} to spend your last few pennies.
Who doesn't like gorging on a budget? {1} has a sweet little spot: {0}!
ALL YOU CAN EAT BUFFET @ {0}, {1}!!!
#michelin are you watching these guys? {0}, {1}!""".replace("<timeframe>", rand_choice(timeframe)).replace("<adjective>", rand_choice(ADJECTIVES)).replace("<pronoun>", rand_choice(PRONOUNS)).split("\n")

tastes = """sour
spicy
fruity
salty
strong flavoured
eggy
piquante
flamin' hot
funky
fermented
sweet
toasty""".split("\n")

food_reviews = """I just love the mouth feel of the {0}!
Be careful, the {0} can be super <taste>
If you like <taste>, go for the {0}.
I can't get enough of the deep fried {0}!
I just love the {0} soup!
Eat all of that {0} now. TELL ALL OF YOUR FRIENDS
My dreams are made of their {0}!
Their {0} is just {1}
The {0} there is simply {1}
{1} {0}. NUFF SAID!
The {0} is absolutely {1}.
If <taste> {0} is your thing, then {1}.
{1} {0}... SUPER SUPER <taste>
<taste> {1}... {0}
I had <number> bowls of the {0} there.
I just scoffed <number> plates of {0} there!
My number #1 is their {0}.
My whole family adores their {0}!
<pronoun> really loves their {0}.
OMG, <pronoun> eats so much {0} when we go there.
The {0} is to die for. SRSLY
If their {0} is the last thing I ever eat I will die happy.
{0}! Doggy bags galore!
Delicious {1} {0}.
SCRUMPTIOUS <taste> {0}.
Gorgeous {0}. When we go, I have to pull <pronoun> away from the plate!!!
Mountains of {0}. {1}
Rivers of {0}. Absolutely {1}!
<pronoun> says I should cut down on my {0} intake. SSSH
I wish I had their {0} recipe.
One day I hope to cook {0} like they do!
{0}, {0} and more {0}!
100% premium {0}.
Plates of amazing, <taste> {0}.
If you like <taste> {0}, this is the joint.
My go-to place for <taste> {0}.
Somewhere I love to eat <taste> {0} with the fam.
A place where I enjoy sampling <taste> {0} alone.
The taste of their {0} is delicious.
It's all about the {1} {0}. Super <taste>.
<pronoun> just won't shut up about their <taste> {0}.
<pronoun> just won't be quiet about their <taste> {0}.
<pronoun> won't stop going on about their <taste> {0}.""".replace("<taste>", rand_choice(tastes)).replace("<pronoun>", rand_choice(PRONOUNS)).replace("<number>", str(randint(3, 20))).split("\n")

hotel_comments = """<timeframe> got back from our stay in {0}, {1}!
<number> {2} days in {0} {1}, <date>
About <number> years back spent some time at a nice hotel - {0} in {1}.
<date>: {0}, {1}. Those were the days!
{2} hotel alert! {0} in {1}!
{0} in {1} is the most {2} hotel.
Want to know where to stay in {1}? {0} is {2}!
Looking for a bed in {1}? Can I recommend {2}?
<date>: {0}, {1}. Well deserved rest.
<date>: {0}, {1}. What a trip!
<date>: {0}, {1}. A 5**** experience!
<timeframe> returned from {1}. Our hotel was {0}.
Can't wait to make it back to {0} in {1}.""".replace("<timeframe>", rand_choice(timeframe)).capitalize().replace("<number>", str(randint(2, 13)).replace("<date>", date+" '"+str(randint(10, 13)))).split("\n")

food_hotel = """Full board. Boy we were stuffed.
Their breakfast was to die for!
All about their breakfast.
Nice restaurant onsite.
Food was good too!
Good, solid meals provided.
Tasty food on offer!
I liked their onsite restaurant.
It was a good place to eat as well.""".split("\n")

def get_extra_tags(terms):
    query = " ".join(terms)
    words = [w for w in query.split(" ") if w not in COMMON]
    return " ".join(["#" + w for w in words])

def get_tags(low, hi):
    tags = sample(TAGS, randint(low//1.5, hi//1.5)) + ["#"+tag for tag in sample(VERBS+NOUNS, randint(low // 3, hi // 3))]
    return " ".join(tags)


def get_random_tripadvisor_caption(venue, locale, type_):
    if type_ == "hotel":
        caption = rand_choice(intros)
        caption += " " + rand_choice(hotel_comments).format(venue, locale, rand_choice(ADJECTIVES))
        if randint(0, 1):
            caption += " " + rand_choice(food_hotel)
            review = rand_choice(food_reviews).format(rand_choice(FOODS), rand_choice(ADJECTIVES))
            caption += " " + review[0] + review[1:]
        else:
            caption += " " + rand_choice(closing_comments)

    elif type_ == "attraction":
        caption = rand_choice(intros) + " " + rand_choice(attraction_quotes).format(venue, locale)
        caption += " " + rand_choice(more_attraction)
        caption += " " + rand_choice(closing_comments)

    else:
        food = rand_choice("foods")
        caption = rand_choice(restaurant_intros).format(venue, locale, food)
        review = rand_choice(food_reviews).format(rand_choice(FOODS), rand_choice(ADJECTIVES))
        caption += " " + review[0] + review[1:]

    caption += " " + "".join(sample(EMOJIS, randint(0, 5)))

    tags = "#"+venue.replace(",", "").replace(" ", "") + " " + "#"+locale.replace(",", "").replace(" ", "") + " #" + rand_choice(adjectives) + rand_choice(NOUNS) + " " + get_tags(1, 4)

    return caption + " " + tags


def get_random_travel_caption(place_name):
    caption = rand_choice(travel_quotes).format(place_name, rand_choice(sights), rand_choice(activities), number, date, rand_choice(adjectives), rand_choice(holiday_equipment))
    emojis = "".join(sample(EMOJIS, randint(1, 3)))
    tags = get_tags(1, 7) + " " + get_extra_tags([place_name.replace(",", "")])

    return caption[0].upper() + caption[1:] + " " + emojis + " " + tags


def get_random_song_caption(song, artist, youtube):
    emojis = "".join(sample(EMOJIS, randint(1, 5)))
    caption = rand_choice(SONG_CAPTIONS).format(song, artist) + " " + emojis + " " + youtube + " " + get_extra_tags([song, "".join(artist.split(" "))]) + " " + get_tags(3, 15)
    return caption[0].upper() + caption[1:]


def get_random_thought():
    pro = rand_choice(PRONOUNS)
    verb = rand_choice(VERBS)
    noun = rand_choice(NOUNS)
    noun2 = rand_choice(NOUNS)
    poss = rand_choice(POSSESSIVES)

    try:
        past_verb = PAST_VERBS[VERBS.index(verb)]
    except:
        past_verb = rand_choice(PAST_VERBS)

    adjectives = rand_choice(ADJECTIVES)

    t = rand_choice(THOUGHTS).replace("<", "{").replace(">", "}").format(pro, verb, poss, noun, noun2, past_verb, adjectives)

    if  not randint(0, 4):
        t = "".join([letter.upper()  if randint(0, 1) else letter.lower() for letter in t])
    else:
        t = t[0].upper() + t[1:]

    tags = get_tags(4, 20)

    tags + " ".join(["#"+ w for w in t.split(" ") if w not in COMMON])

    emojis = rand_choice(EMOJIS)

    if not randint(0, 2):
        emojis += rand_choice("?!")

    if not randint(0, 2):
        emojis += rand_choice(EMOJIS)

    if not randint(0, 2):
        emojis += rand_choice(EMOJIS)


    return t + " " + emojis + " " + tags


