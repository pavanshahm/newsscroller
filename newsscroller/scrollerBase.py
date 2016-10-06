from newsCollection import newsCollection
from displayStream import displayStream

class scrollerBase:
    """ Class that manages data input and output"""

    def __init__(self):
        #self.allNews = newsCollection()
        self.stream = displayStream()