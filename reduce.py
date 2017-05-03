#decorator function name
def getInfo(func):
    def innerFunc(*param):
        print func.__name__ + "(" + str(*param) + ")"+":"
        return func(*param)
    return innerFunc

#init book
book  = open("book.txt", "r").read().split()
book = [x.translate(None, ".,!?()\'\"") for x in book]
book = [x.lower() for x in book]
book = book[0:12345]

@getInfo
def wordFreq(word):
  return len(filter(lambda x: x == word, book))

@getInfo
def groupFreq(words):
  return len(filter(lambda x: True if x in words else False, book))

words = {}
def count(word):
  if word not in words.keys():
    words[word] = len(filter(lambda x: x == word, book))
  return word

@getInfo
def mostFreq():
  map(count, book)
  out = sorted(words.items(), key=lambda x: x[1])
  return out[1]

print wordFreq("the")
print groupFreq(["life","history"])
print mostFreq()