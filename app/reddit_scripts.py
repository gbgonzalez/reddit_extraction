from database.connect import database_connect
from models import Post
import datetime as dt
import argparse
from extraction.extract_data import extract_data
from refresh.refresh import refresh_token


if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--option", type=str, help="select an option")
    parser.add_argument("-s", "--subreddit", type=str, help="name of subreddit", required=True)
    parser.add_argument("-d", "--database", type=str, help="name of database", required=True)
    parser.add_argument("-q", "--query", type=str, help="word to search", required=False)


    args = parser.parse_args()

    if args.option == "extraction_last_posts":
        # python app\reddit_scripts.py -o extraction_last_posts -s Anxiety -d reddit

        session = database_connect(args.database)
        extract_data(session, args.subreddit, "last_posts")

    if args.option == "extraction_search":
        # python app\reddit_scripts.py -o extraction_last_posts -s Anxiety -d reddit -q example_search

        session = database_connect(args.database)
        search = args.query
        extract_data(session, args.subreddit, "search", search)

    if args.option == "extraction_search_by_flair":
        # python app\reddit_scripts.py -o extraction_search_by_flair -s Anxiety -d reddit

        """ ANXIETY """
        flairs = ["Discussion", "DAE Questions", "Health", "Venting", "Uplifting", "Anxiety", "Resource",
                  "Needs A Hug/SupportSleep", "Advice Needed", "Medication", "Work/School"]

        session = database_connect(args.database)
        extract_data(session, args.subreddit, "search_by_flair", flairs)

    if args.option == "refresh_token":
        # python app\reddit_scripts.py -o refresh_token

        refresh_token()

