from textblob import TextBlob
import tweepy
import pandas as pd

class Mood:
    def __init__(self, mood:str, sentiment:float):
        self.mood = mood
        self.sentiment = sentiment
    
def get_mood(input_text:str, threshold:float) -> Mood:
    sentiment:float = TextBlob(input_text).sentiment.polarity
    
    friendly_threshold:float = threshold
    hostile_threshold:float = -threshold
    
    if sentiment >= friendly_threshold:
        return Mood('friendly', sentiment)
        
    elif sentiment <= hostile_threshold:
        return Mood('hostile', sentiment)
        
    else:
        return Mood('neutral', sentiment)


df = pd.read_csv('tweets1.csv')
tweet_snippets = df['snippet']

polarity = 0

for tweet in tweet_snippets:
    mood = get_mood(tweet, 0.5)
    print(mood.mood)
    
print(polarity)


