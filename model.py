__author__ = 'Zhou Yumin'
import numpy as np
import scipy as sp
from sklearn import linear_model
from sklearn.ensemble import GradientBoostingClassifier
import betting as bt
import matplotlib.pyplot as plt

# feature0 = np.loadtxt('F:\data\Season2010feature.txt')
# result0 = np.loadtxt('F:\data\Season2010class.txt')
feature1 = np.loadtxt('F:\data\Season2011feature.txt')
result1 = np.loadtxt('F:\data\Season2011class.txt')
feature2 = np.loadtxt('F:\data\Season2012feature.txt')
result2 = np.loadtxt('F:\data\Season2012class.txt')
feature3 = np.loadtxt('F:\data\Season2013feature.txt')
result3 = np.loadtxt('F:\data\Season2013class.txt')

feature = np.vstack((feature1, feature2, feature3))
result = np.concatenate((result1, result2, result3))

data = np.loadtxt('F:\data\Season2014feature.txt')
truth = np.loadtxt('F:\data\Season2014class.txt')
odds = np.loadtxt('F:\data\Season2014odds.txt')

# print feature.transpose()[0]

logreg = linear_model.LogisticRegression()

logreg.fit(feature, result)

# adb = GradientBoostingClassifier()
# adb.fit(feature, result)
# predAda = adb.predict(data)
# print predAda
# print bt.accuracy(predAda, truth)
# print bt.gain(predAda, truth, odds)

# Naive Strategy
predNaive = logreg.predict(data)
allOddFavourWin = 2 - np.argmin(odds, axis=1)
prob = logreg.predict_proba(data)
predBest = bt.bestStrategy(prob, odds)
print len(predNaive)
print predNaive
print predBest
print truth
print truth.size
print bt.accuracy(predNaive, truth)
print bt.accuracy(predBest, truth)
print bt.gain(predNaive, truth, odds)
print bt.gain(predBest, truth, odds)

#print prob.transpose()[0]
#plt.plot(feature.transpose()[13], prob.transpose()[1], 'o')
#plt.show()




