import pandas as pd
import numpy as np
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
import pickle
def main():

    df = pd.read_table(
        "./tsvs/var.tsv",
        sep="    ",
        header=None,
        names=["label", "message"],
        engine="python",
    )

    df["label"] = df.label.map({"yes": 1, "no": 0})

    df["message"] = df.message.map(lambda x: str(x).lower())

    df["message"] = df.message.str.replace("[^\w\s]", "")

    
    df["message"] = df["message"].apply(nltk.word_tokenize)

   

    stemmer = PorterStemmer()

    df["message"] = df["message"].apply(lambda x: [stemmer.stem(y) for y in x])

    # This converts the list of words into space-separated strings
    df["message"] = df["message"].apply(lambda x: " ".join(x))
    # df = clean_dataset(df)

    count_vect = CountVectorizer()
    counts = count_vect.fit_transform(df["message"])

    transformer = TfidfTransformer().fit(counts)

    counts = transformer.transform(counts)

    X_train, X_test, y_train, y_test = train_test_split(
        counts, df["label"], test_size=0.1, random_state=69
    )


    model = MultinomialNB().fit(X_train, y_train)


    predicted = model.predict(X_test)

    print(np.mean(predicted == y_test))


    print(confusion_matrix(y_test, predicted))

    with open("model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)


main()
