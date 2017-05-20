import matplotlib.pyplot as plt
import numpy as np
import random

#conmand: np.random.normal(mu, sigma, size)

mu = 5
sigma = 2
size = 1000
ran = 10 * np.random.normal(mu, sigma, size)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#plot histogram
n, bins, patches = ax1.hist(ran,bins=80,color="#00A9AE", normed = True);
ax1.set_xlabel('value')
ax1.set_ylabel('occurance')

fig.show()