#practice-1 in Monte Carlo Tutorial

import matplotlib.pyplot as plt
import numpy as np
import random

#(a)
#generate 1000 randon numbers between [0,1]

ran = [];

for i in range (1000):
    ran.append(random.random());

#plot histogram
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

n, bins, patches = ax1.hist(ran,bins=100,color="#00A9AE");
ax1.set_xlabel('value') 
ax1.set_ylabel('occurance')

#(b)
#generate 1000 randon numbers between [1,15]
ran = [];

for i in range (1000):
    ran.append(random.random() * 14 + 1);

#plot histogram
n, bins, patches = ax2.hist(ran,bins=80,color="#205d8a");
ax2.set_xlabel('value')
ax2.set_ylabel('occurance')

fig.show()