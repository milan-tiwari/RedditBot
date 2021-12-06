from redditors import redditor_functions as rf
from subreddit import subreddit_functions as sf

print(" 1: REDDITOR INFORMATION\n",
      "2: SUBREDDIT INFROMATION\n",
      "YOUR CHOICE: ")

choice = int(input())
#choice = 2

def menu(c):
    if not(c>0 or c<5):
        return 0

    if c==1:
        rf1 = rf()
        rf1.stuff()
        print("FIND YOUR REDDITOR INFO IN creds.txt")

    if c==2:
        sf1 = sf()
        sf1.top_subs()
        print("FIND YOUR SUBREDDIT INFO IN subs.txt")
menu(choice)


