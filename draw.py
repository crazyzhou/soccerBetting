import numpy as np
from matplotlib import pyplot as plt

labels = ['lsrH', 'lsrA', 'rGH', 'rGA', 'rAGH', 'rAGA', 'rStH', 'rStA', 'rAStH', 'rAStA', 'rCoH', 'rCoA', 'rACoH',
          'rACoA', 'klH', 'klD', 'klA', 'avOH', 'avOD', 'avOA', 'OH', 'OD', 'OA']

data = np.loadtxt('F:\data\Season2014feature.txt')
a = np.corrcoef(data.transpose())

print a.shape
fig, ax = plt.subplots()
heatmap = plt.pcolor(a)

ax.set_xticks(np.arange(23)+0.5)
ax.set_yticks(np.arange(23)+0.5)
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

plt.colorbar()
plt.show()