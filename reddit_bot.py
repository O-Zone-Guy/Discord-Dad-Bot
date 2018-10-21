import praw
import sql_handler

__username = 'dad-sweeper-bot'
__pass = 'e8EV7EgcRe2Xd5x'
__client_id = 'wk6O38PhWWdj3g'
__client_secret = 'rMulU-xNj6Ue9Ah7FSxlgNMYvb8'

r = praw.Reddit(username=__username,
                password=__pass,
                client_id=__client_id,
                client_secret=__client_secret,
                user_agent="Dad Jokes sweeper V0.1")


def get_jokes():
    for post in r.subreddit('dadjokes').hot(limit=100):
        sql_handler.insert_joke(post_id=post.id, title=post.title, body=post.selftext, author=post.author)
        pass
    pass


get_jokes()

while True:
    pass
