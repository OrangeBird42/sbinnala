#project start 1/23/23 
print("Welcome to Khonjin A Day!")
import random

readEpisode = open('episodeList.txt', "r")
#readEpisodeContents = readEpisode.read()
#print(readEpisodeContents)

#readEpisode.close()

#with open("episodeList.txt", "r") as file:
 #   allText = file.read()
  #  word = list(map(str, allText.split()))

   # print(random.choice(word))


def random_line(episodeList):
    lines = open(episodeList).read().splitlines()
    return random.choice(lines)
print(random_line('episodeList.txt'))

readEpisode.close()