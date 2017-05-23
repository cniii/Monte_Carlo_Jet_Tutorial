import matplotlib.pyplot as plt
import numpy as np
import random

#expoential decay: np.random.exponential(scale, size)

ranexp = np.random.exponential(1, 50);

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#plot histogram
n, bins, patches = ax1.hist(ranexp,bins=80,color="#00A9AE");
ax1.set_xlabel('value')
ax1.set_ylabel('occurance')

fig.show()