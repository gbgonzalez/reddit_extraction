from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
import os

def database_connect(target: str):

    engine = create_engine(
        f"mysql+pymysql://redditUser:redditPass@localhost:3306/{target}?charset=utf8mb4"
    )
    Session = sessionmaker(bind=engine, autoflush=False)

    return Session()

def database_engine(target: str = "colorectal"):
    if target == "corona":
        engine = create_engine(
            #"mysql+pymysql://tweetUser:tweetPass@192.168.200.134:3306/tweet_corona?charset=utf8mb4"
            "mysql+pymysql://tweetUser:tweetPass@localhost:3306/tweet_corona?charset=utf8mb4"
        )
    elif target ==  "crc_analysis":
        engine = create_engine(
            "mysql+pymysql://tweetUser:tweetPass@localhost:3306/crc_ner_analysis?charset=utf8mb4"
        )
    elif target ==  "corona_es":
        engine = create_engine(
            "mysql+pymysql://tweetUser:tweetPass@localhost:3306/tweet_corona_esp?charset=utf8mb4"
        )
    elif target ==  "covid_analysis":
        engine = create_engine(
            "mysql+pymysql://tweetUser:tweetPass@localhost:3306/covid_analysis?charset=utf8mb4"
        )
    elif target ==  "misinformation_covid":
        engine = create_engine(
            "mysql+pymysql://tweetUser:tweetPass@localhost:3306/misinformation_covid?charset=utf8mb4"
        )
    elif target ==  "cancer":
        engine = create_engine(
            "mysql+pymysql://tweetUser:tweetPass@localhost:3306/tweet_mining?charset=utf8mb4"
        )
    else:
        engine = create_engine(
            f"mysql+pymysql://tweetUser:tweetPass@localhost:3306/{target}?charset=utf8mb4"
        )

    return engine