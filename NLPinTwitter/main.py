import tweepy
import configparser

# Configure ConfigParser
conf=configparser.ConfigParser()
conf.read('./NLPinTwitter/config.ini')

# Twitter APIキーを設定
consumer_key = conf['NLPinTwitter']['API_KEY']
consumer_secret = conf['NLPinTwitter']['API_SECRET']
access_token = conf['NLPinTwitter']['ACCESS_TOKEN']
access_token_secret = conf['NLPinTwitter']['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# 特定のキーワードに関するツイートを検索
tweets = tweepy.Cursor(api.search_tweets, q='BITCOIN', lang='ja', tweet_mode='extended').items(1000)
tweets_text = [tweet.full_text for tweet in tweets]

import nlplot
import pandas as pd

# リストからDataFrameを作成
df_tweets = pd.DataFrame(tweets_text, columns=['text'])

npt = nlplot.NLPlot(df_tweets, target_col='text')

# 単語の出現回数をカウントして表示
npt.bar_ngram(title='counts of words', ngram=1, top_n=30)

# 共起ネットワークを作成して表示
npt.build_graph(min_edge_frequency=10)
npt.co_network(title='Co-occurrence network')

# 主題の分布をトピックモデリングで表示
#npt.build_topic_model(num_topics=5, num_words=5)
#npt.topic_heatmap(title='Topics heatmap')

# 主題ごとの単語の分布を表示
npt.word_distribution(title='Word Distribution per Topic')

npt.show()