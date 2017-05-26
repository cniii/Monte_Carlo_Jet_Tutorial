import matplotlib.pyplot as plt
import numpy as np
import random
import math #sqrt

#conmand: np.random.normal(mu, sigma, size)
"""
mu = 5
sigma = 2
size = 1000
ran = 10 * np.random.normal(mu, sigma, size)


"""
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


"""
How to generate gaussian distribution using Accept-Reject?
def PDF(x):
    return math.sqrt(2/L) * math.sine(math.pi * x / L)     
"""



size = 10000;
L = 10;
x = [];

def PDF(x):
    return math.sqrt(2.0/L) * math.sin(math.pi * x / L)

for i in range (size):
    x.append(10 * random.random())
    
for temp in x:
    y = random.random();
    if PDF(temp) < y:
        x.remove(temp);
       
                              

#plot histogram
n, bins, patches = ax1.hist(x,bins=80,color="#00A9AE", normed = True);
ax1.set_xlabel('value')
ax1.set_ylabel('occurance')

fig.show()