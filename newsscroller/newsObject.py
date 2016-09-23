class newsObject(object):
    """description of class"""
    def __init__():
        reset()

    def reset():
        self.articles = []
        self.iter = -1

    def getIter():
        return self.iter

    def add(title, article):
        self.articles.insert(tuple(title, article))

    def __getitem__(self, index):
        return self.articles[index]
    
    def length():
        return len(self.articles)

    def pop():
        return self.articles.pop()