import pandas
from sklearn import preprocessing
from yellowbrick.features import Rank1D, Rank2D
from yellowbrick.features.pca import PCADecomposition
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split

columns = ["duration","protocol_type","service","flag","src_bytes",
"dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
"logged_in","num_compromised","root_shell","su_attempted","num_root",
"num_file_creations","num_shells","num_access_files","num_outbound_cmds",
"is_host_login","is_guest_login","count","srv_count","serror_rate",
"srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
"diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
"dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
"dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty"]

data = pandas.read_csv('ids_dataset/NSL_KDD-master/KDDTrain+.csv', 
        header=None, names=columns)

data.describe()

data.protocol_type = preprocessing.LabelEncoder().fit_transform(data['protocol_type'])
data.service = preprocessing.LabelEncoder().fit_transform(data['service'])
data.flag = preprocessing.LabelEncoder().fit_transform(data['flag'])
data.label = preprocessing.LabelEncoder().fit_transform(data['label'])

X = data[columns].values
y = data.label.values

"""
visualizer = Rank1D(features=columns, algorithm='shapiro')
visualizer.fit(X, y)
visualizer.transform(X)
visualizer.poof()

visualizer = Rank2D(features=columns, algorithm='covariance')
visualizer.fit(X, y)
visualizer.transform(X)
visualizer.poof()

visualizer = Rank2D(features=columns, algorithm='pearson')
visualizer.fit(X, y)
visualizer.transform(X)
visualizer.poof()

visualizer = PCADecomposition(scale=True, center=False, col=y)
visualizer.fit_transform(X, y)
visualizer.poof()

visualizer = PCADecomposition(scale=True, center=False, col=y, proj_dim=3)
visualizer.fit_transform(X, y)
visualizer.poof()
"""

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
score = clf.score(X_test, y_test)

print("Score:",score*100)
