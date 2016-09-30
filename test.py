import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

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
prob = logreg.predict_proba(data)

plt.plot(data.transpose()[3], prob.transpose()[0], '.r', label='Score')
plt.plot(data.transpose()[5], prob.transpose()[0], '.b', label='Concede')
# plt.plot(data.transpose()[16], prob.transpose()[0], '.g', label='AwayWin')
# plt.axis([25, 90, 0, 1])
# plt.title("Home Advantage")
plt.xlabel("Recent Goal Score/Concede of Home Team")
plt.ylabel("Predicted Probability of Home Win")
plt.legend(loc='lower right')
plt.show()