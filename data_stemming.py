import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')

column_names = ['target', 'id', 'date', 'flag', 'user', 'text']
df = pd.read_csv('dataset.csv', names=column_names, encoding='ISO-8859-1')

df.replace({'target':{4:1}}, inplace=True)

#stemming
port_stem = PorterStemmer()

def stemming(content):

    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)

    return stemmed_content

df['stemmed_content'] = df['text'].apply(stemming)

df.to_csv('modified_data.csv')