import sys
import random
import math
import matplotlib.pyplot as plt
import TAS_diagram

TAS_diagram.TAS()
x=[50,60,70,45]
y=[8,9,10,11]
plt.scatter(x,y,s=500,alpha=0.5,color='g',marker='D')
plt.savefig('TAS.jpg')