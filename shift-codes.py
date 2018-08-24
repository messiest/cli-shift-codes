import feedparser
from bs4 import BeautifulSoup

SHIFT_FEED = "https://feeds.feedburner.com/disdain/shiftcodes/xbox"

d = feedparser.parse(SHIFT_FEED)




if __name__ == "__main__":
    for i in d['entries']:
        b = BeautifulSoup(i['summary'], 'lxml')

        content = b.find('b').text
        msg_parts = content.split('\n')
        print(msg_parts[0])
