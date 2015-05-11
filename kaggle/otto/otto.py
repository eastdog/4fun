#coding: utf-8
__author__ = 'eastdog'

import pandas as pd
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier

class Otto():

    def __init__(self):

        self.labels = set()
        self.model = None

    def train(self, inpath):

        data = pd.read_csv(inpath)
        X = data.ix[:, 1:-1].values
        Y = data.ix[:, -1].values
        self.labels = sorted(set(Y))
        self.model = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
        # clf2 = DecisionTreeClassifier(max_depth=None, min_samples_split=1, random_state=0)
        # self.model = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
        self.model.fit(X, Y)
        # clf = GradientBoostingClassifier(n_estimators=100)
        print cross_val_score(self.model, X, Y).mean()
        # clf1 = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)

    def predict(self, testpath, outpath):

        with open(outpath, 'w') as fo:
            fo.write('id,%s\n'%(','.join(self.labels)))
            for line in pd.read_csv(testpath).ix[:, :].values:
                label = self.model.predict(line[1:])
                fo.write('%s,%s\n'%(line[0], ','.join([str(int(label[0] == x)) for x in self.labels])))

if __name__ == '__main__':

    otto = Otto()
    otto.train('train.csv')
    otto.predict('test.csv', 'out.csv')

# 1st, ExtraTreeClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0), 7.39
# 2nd, RandomForestClassifier(n_estimators=10, max_depth=10, min_samples_split=1, random_state=0), 10.48