import praw
import sql_handler
import config

r = praw.Reddit(username=config.reddit_username,
                password=config.reddit_pass,
                client_id=config.reddit_client_id,
                client_secret=config.reddit_client_secret,
                user_agent="Dad Jokes sweeper V0.1")


def get_jokes():
    for post in r.subreddit('dadjokes').hot(limit=100):
        sql_handler.insert_joke(post_id=post.id, title=post.title, body=post.selftext, author=post.author)


get_jokes()
