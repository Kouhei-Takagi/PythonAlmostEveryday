import feedparser

url = 'https://www.j-platpat.inpit.go.jp/cache/rss/patent/2020/2020003001/2020003965.xml'

feed = feedparser.parse(url)

print(feed)
