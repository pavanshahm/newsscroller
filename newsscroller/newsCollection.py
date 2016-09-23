import newspaper
import newsObject

from newspaper import Article

class newsCollection(object):
    """Provides Abstraction for all the NewsPaper API stuff including validations"""
    def  __init__():
        self.news = newsObject()

    def initNews(firstTime):
        print("Hello World")
        paper = newspaper.build('http://gamnesia.com', memoize_articles=firstTime)

        if not firstTime:
            self.news.reset()

        for article in paper.articles:
            print(article.url)
    
        for article in paper.articles:
            url = article.url
            a = Article(url)
            a.download()
            a.parse()
            try:
                self.news.add(a.title, a.text)
            except:
                pass

    def pop():
        return self.news.pop()
    
    def empty():
        return self.news.lenght() == 0