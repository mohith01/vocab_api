import requests
from bs4 import BeautifulSoup

def get_list(url):
    r = requests.get(url)
    b = BeautifulSoup(r.content,features="lxml")
    list1 = b.select('.dynamictext')
    for i in range(len(list1)):
        list1[i] = list1[i].text

    return res[1:]

class Word():
    def __init__(self,word1):
        r  = requests.get('https://www.vocabulary.com/dictionary/'+word1)
        soup = BeautifulSoup(r.content,features="lxml")
        self.word = word1
        self.short_desc = soup.select('.short')
        self.long_desc = soup.select('.long')
        self.similar = soup.select("ol li")

    def as_dict(self):
        return {'word': self.word,'short_desc':self.short_desc, 'long_desc': self.long_desc, 'similardef':self.similar}


