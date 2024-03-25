import pandas as pd
import requests

twitter_data = []

payload = {
    'api_key':'',
    'query':'crypto',
    'num':'100'    
}
response = requests.get(
    'https://api.scraperapi.com/structured/twitter/search', params=payload
)
data = response.json()

all_tweets = data['organic_results']
for tweet in all_tweets:
    twitter_data.append(tweet)
    
df = pd.DataFrame(twitter_data)
df.to_json('tweets1.json', orient='index')