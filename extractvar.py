import RAKE
import operator
import nltk
from nltk.tokenize import word_tokenize
import json
import re

with open("stoplist.json") as f:
    stoplist = json.load(f)


class Variable:
    def __init__(self, text):
        global stoplist
        self.text = text
        self.namelookup = ["NNP", "NNS", "NN", "JJS", "JJ"]
        self.stoplist = stoplist["variable"]
        self.tmp = ""
    def name(self):
        self.stop_dir = "./stoplist.txt"
        self.rake_object = RAKE.Rake(self.stop_dir)
        self.keywords = self.sort_tup(self.rake_object.run(self.text)[-10:])
        print("KEYWORDS: ", self.keywords)

    def sort_tup(self, tup):
        tup.sort(key=lambda x: x[1])
        return tup

    def name_nltk(self):
        self.tmp = word_tokenize(self.text)
        self.words = nltk.pos_tag(self.tmp)
        self.words = [i for i in self.words if i[0] not in self.stoplist]
        self.words = [i for i in self.words if i[1] in self.namelookup]
        print(self.words)
    def get_value(self):
        if self.text.count('"') == 2 or self.text.count("'") == 2:
            tmp = re.findall(r"\'(.+)\'", self.text)
            if len(tmp) == 0:
                tmp = re.findall(r'\"(.+)\"',self.text)
            return tmp[0]
        for i in ["True","true","False","false"]:
            if i in self.text:
                return i
        self.tmp = word_tokenize(self.text)
        self.words = nltk.pos_tag(self.tmp)
        self.words = [i for i in self.words if i[0] not in self.stoplist]
        for i in self.words:
            if i[1] == "CD":
                return i[0]
class MakeRegex:
    def __init__(self):
        pass


imp = Variable("set the value of x to 5")
imp.name_nltk()
print(imp.get_value())
imp = Variable("apples = 5")
imp.name_nltk()
print(imp.get_value())
imp = Variable("set the value of x to false")
imp.name_nltk()
print(imp.get_value())
imp = Variable("create a new variable named apples, and set its value to 5")
imp.name_nltk()
print(imp.get_value())
imp = Variable("the value of xtwo is 3")
imp.name_nltk()
print(imp.get_value())
imp = Variable("decTest = 5.64")
imp.name_nltk()
print(imp.get_value())
imp = Variable("d4 equal 5.64")
imp.name_nltk()
print(imp.get_value())
imp = Variable("say 'hello'")
imp.name_nltk()
print(imp.get_value())