from random import randint
from time import sleep
from main import place_or_music_or_thought

from datetime import datetime

def schedule():

    time = 0

    while True:

        sleep(10)



        variance = randint(-300, 300)
        if time % ((60 * 60) + variance) == 0:
            try:
                place_or_music_or_thought()
                print("Time is {}. Did a post.".format(datetime.now()))
            except Exception as e:
                print(e)
                sleep(15)
                time = 0

        time += 1


if __name__ == "__main__":

    schedule()
