"""
    dataset from: https://labs-repos.iit.demokritos.gr/skel/i-config/
"""

from nltk import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import NaiveBayesClassifier, classify

stop = stopwords.words('english')

def Process(data):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in 
            word_tokenize(unicode(data, errors='ignore'))]

def Features_Extraction(text, setiing):
    if setting == 'bow':
        return {word: count for word,count in Counter(Process(text) if not
            word in stop)}
    else:
        return {word: True for word in Process(text) if not word in stop}

features = [(Features_Extraction(email, 'bow'), label) for (email, label)
        in emails]

def training_Model(Features, samples):
    size = int(len(Features) * samples)
    training, testing = Features[:size], Features[size:]
    print('Training: ' + str(len(training)) + ' emails')
    print('Testing: ' + str(len(testing)) + ' emails')
    classifier = NaiveBayesClassifier.train(training)

def evaluate(training, testing, classifier):
    print('Training Accuracy: ' + str(classify.accuracy(classifier,
        training)))
    print('Testing Accuracy: ' + str(classify.accuracy(classifier, testing)))

