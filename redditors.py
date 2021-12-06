"""
contains functions for redditor class instance
secret key : n-lbAOq5hYGM3Ogp2t7kNR5kpSL6EA
client id : Y9JYxyhhhbVvJw
confidential to individual developer
"""

import praw as pw
from prawcore import exceptions as EX
from datetime import datetime

reddit = pw.Reddit(
    client_id = "Y9JYxyhhhbVvJw",
    client_secret = "n-lbAOq5hYGM3Ogp2t7kNR5kpSL6EA",
    user_agent = "MandoBoi_0"
)
#Top-Two5926
class redditor_functions:

    def __user(self):
        #ruser = input("REDDITORS HANDLE:").split()
        ruser = "Top-Two5926"
        try:
            return reddit.redditor(str(ruser))
        except EX.NotFound:
            print("USER NOT FIND")
            self.__user()


    def stuff(self):
        user = self.__user()
        f = open("creds.txt","w+")
        #name
        f.write("NAME: %s\n"%user.name)

        #user should be verified first
        try:
            is_verified = user.has_verified_email
        except EX.ServerError:
            print("VERFIY EMAIL FIRST")
            return

        #karma
        f.write("Karma: %s\n" % user.link_karma)

        #is mod in any subreddit
        f.write("ID: %s\n" %user.id)
        if(user.is_mod):
            f.write("%s is a mod\n"%user.name)
        else:
            f.write("%s is not a mod\n" % user.name)

        #time of joining
        time = datetime.utcfromtimestamp(user.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        f.write("Joining time %s\n" %time)

        #checking user subreddit

        if(user.subreddit):
            f.write("\n\nSUBREDDIT DETAILS\n")
            f.write("Title: %s\n" %str(user.subreddit["title"]))
            f.write("Description: %s\n" % str(user.subreddit["public_description"]))
            f.write("Subscribers count: %s\n" % str(user.subreddit["subscribers"]))
            f.write("NSFW: %s\n" % str(user.subreddit["over_18"]))
            if(user.subreddit["banner_img"]):
                f.write("Banner url: %s\n" % str(user.subreddit["banner_img"]))
        else:
            f.write("USER DONT HAVE A SUBREDDIT\n")

        #USER COMMENTS
        f.write("\n\nTOP USER COMMENTS\n")
        for comments in user.comments.hot(limit=3):
            f.write("%s\n" %comments.body)




