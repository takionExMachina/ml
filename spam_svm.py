import os
import numpy
from collections import Counter
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

def make_dictionary(train_dir):
    emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i,line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    list_to_remove = dictionary.keys()
    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(3000)
    return dictionary

def extract_features(mail_dir):
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    feature_matrix = numpy.zeros((len(files), 3000))
    docID = 0
    for fil in files:
        with open(fil) as fi:
            for i,line in enumerate(fi):
                if i == 2: 
                    words = line.split()
                    for word in words:
                        wordID = 0
                        for i,d in enumerate(dictionary):
                            if d[0] == word:
                                wordID = i
                                features_matrix[docID, wordID] = words.count(word)
            docID = docID + 1
    return features_matrix

train_dir = '<train_mails dir>'
dictionary = make_dictionary(train_dir)

train_labels = numpy.zeros(702)
train_labels[351:701] = 1
train_matrix = extract_features(train_dir)

model = LinearSVC()
model.fit(train_matrix, train_labels)

test_dir = '<test_mails dir>'
test_matrix = extract_features(test_dir)
test_labels = numpy.zeros(260)
test_labels[130:260] = 1

result =  model.predict(test_matrix)
print confusion_matrix(test_labels, result)
