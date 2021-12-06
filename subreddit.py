import praw as pw
from prawcore import exceptions as EX

reddit = pw.Reddit(
    client_id="Y9JYxyhhhbVvJw",
    client_secret="n-lbAOq5hYGM3Ogp2t7kNR5kpSL6EA",
    user_agent="MandoBoi_0"
)

subreddit = reddit.subreddit("redditdev")


class subreddit_functions:

    def top_subs(self):
        f = open("subs.txt", "w+")
        for subs in subreddit.hot(limit=5):
            f.write("%s\n" % str(subs.title))
