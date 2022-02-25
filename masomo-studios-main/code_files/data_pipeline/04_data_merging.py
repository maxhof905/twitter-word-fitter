

import pandas

with open('../data_files/tweets_processed.tsv', 'r') as file:
    tagged_tweets = [line for line in file]
    tagged_tweets = tagged_tweets[2:]
    # print(tagged_tweets)

df = pandas.read_csv('../data_files/tweets_cleaned.csv')
df['tagged_tweets'] = tagged_tweets
#df = df.drop(['id'], axis=1)
#print(df.head())

df.to_csv('../data_files/tweets_merged.csv', index=False, header=True)
          #index=True, index_label='index')
