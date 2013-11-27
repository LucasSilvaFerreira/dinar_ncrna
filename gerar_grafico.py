orf_sizes_vector=open('dinar_ncrna_1000_embaralhado.txt','r').read()
vetor=[]
for x in orf_sizes_vector.split('\n'):
      vetor.append(float(x)/3424)

print len(vetor)

import matplotlib.pyplot as plt

import matplotlib.pyplot as hist
#plt.plot(vetor,fmt)
#plt.ylabel('some numbers')
from collections import Counter
print Counter(vetor)
#plt.show()
#print vetor
from pylab import *
hash=Counter(vetor)
#sorted(d.items(), key=lambda x: x[1])
print sort(hash.items())
plot_x=[]
plot_y=[]
for item in hash.items():
      plot_x.append(item[0])
      plot_y.append(item[1])
#subplot(plot_x,'r')
#show()
#hist.(vetor,normed=True)
#hist.show()

import numpy as np
import matplotlib.pyplot as plt

alphab = plot_x
frequencies = plot_y

pos = np.arange(len(alphab))
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
#ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(alphab)

plt.bar(pos, frequencies, color='r')
plt.show()