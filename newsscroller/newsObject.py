class newsObject(object):
    """description of class"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.articles = []
        self.iter = -1

    def getIter(self):
        return self.iter

    def add(title, article):
        self.articles.insert(tuple(title, article))

    def __getitem__(self, index):
        return self.articles[index]
    
    def length(self):
        return len(self.articles)

    def pop(self):
        return self.articles.pop()