import newspaper
from newspaper import Article

def main():
    print("Hello World")
    cnn_paper = newspaper.build('http://gamnesia.com', memoize_articles=False)

    for article in cnn_paper.articles:
        print(article.url)
    
    for article in cnn_paper.articles:
        url = article.url
        a = Article(url)
        a.download()
        a.parse()
        print(a.title)
        print(a.text[:150])



if __name__ == "__main__":
	main()