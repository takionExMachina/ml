import numpy
from sklearn import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""
    Data from https://archive.ics.uci.edu/ml/datasets/Phishing+Websites

    attributes:
        having_IP_address -1,1
        URL_length 1,0,-1
        Shortining_Service 1,-1
        having_At_Symbol 1,-1
        double_slash_redirecting -1,1
        Prefix_Suffix -1,1
        having_Sub_Domain -1,0,1
        SSLfinal_State -1,1,0
        Domain_registration_length -1,1
        Favicon 1,-1
        port 1,-1
        HTTPS_token -1,1
        Request_URL 1,-1
        URL_of_Anchor -1,0,1
        Links_in_tags 1,-1,0
        SFH -1,1,0
        Submitting_to_email -1,1
        Abnormal_URL -1,1
        Redirect 0,1
        on_mouseover 1,-1
        RightClick 1,-1
        popUpWindow 1,-1
        Iframe 1,-1
        age_of_domain -1,1
        DNSRecord -1,1
        Google_Index 1,-1
        Links_pointing_to_page 1,0,-1
        Statistical_report -1,1
        Result -1,1
"""

training_data = numpy.genfromtxt('dataset.csv', delimiter=',', dtype=numpy.int32)

inputs = training_data[:,:-1]
outputs = training_data[:,-1]

training_inputs = inputs[:2000]
training_outputs = outputs[:2000]
testing_inputs = inputs[2000:]
testing_outputs = outputs[2000:]

classifier = LogisticRegression()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)

accuracy = 100.0*accuracy_score(testing_outputs, predictions)
print('The accuracy is: ' + str(accuracy))
