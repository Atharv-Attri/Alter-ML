import pickle
import time
from textblob import TextBlob
t1 = time.time()
cl = pickle.load( open( "classifier.pickle", "rb" ) )
print("Loading took: ",time.time()-t1)
t1 = time.time()
blob = TextBlob("while x is 1:", classifier=cl)
print(blob.classify())
print("Classifying took: ",time.time()-t1)
t1 = time.time()
blob = TextBlob("x=4", classifier=cl)
print(blob.classify())
print("Classifying took: ",time.time()-t1)
t1 = time.time()
blob = TextBlob("name = 'hello'", classifier=cl)
print(blob.classify())
print("Classifying took: ",time.time()-t1)
