import pickle
import sys

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import RidgeClassifier, SGDClassifier
from sklearn.metrics import classification_report
from sklearn.multioutput import MultiOutputClassifier
from sklearn.compose import ColumnTransformer

from sentistrength import getSentiment
from load_dataset import load_dataset

pip = None

def train(datasetName):
    global pip
    datasetPath = '../data/' + datasetName
    modelPath = '../data/' + datasetName + 'Model.pkl'

    x, y = load_dataset(datasetPath)#pickle.load(open('tmp2.pkl', 'rb'))#
    pickle.dump((x, y), open('./tmp2.pkl', 'wb'))
    
    pip = Pipeline([
        ('vect', ColumnTransformer([
            ('tfidf', TfidfVectorizer(sublinear_tf=True), 0),
            ('senti', Normalizer(), [1])])),
        ('clf', MultiOutputClassifier(SGDClassifier(class_weight="balanced", random_state=13)))
    ])
    pip.fit(x, y)

    x, y = load_dataset(datasetPath, test=True)

    y_true_tracker, y_true_urgence = zip(*y)
    y_pred_tracker, y_pred_urgence = zip(*pip.predict(x))
    
    print("tracker:")
    print(classification_report(y_true_tracker, y_pred_tracker))
    print("urgence:")
    print(classification_report(y_true_urgence, y_pred_urgence))

    pickle.dump(pip, open(modelPath, 'wb'))

def run(datasetName, x):
    global pip
    modelPath = '../data/' + datasetName + 'Model.pkl'

    if(not pip):
        try:
            pip = pickle.load(open(modelPath, 'rb'))
        except:
            train(datasetName)

    x = [x, *getSentiment(x)]

    return pip.predict([x])[0]

if __name__ == '__main__':
    print(run(sys.argv[1], sys.argv[2]))