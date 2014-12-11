import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy
plt = pyplot

from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

from pylab import *
from numpy import *

def TAS():
    fig = plt.figure(figsize=(16,10.28))
    ax = fig.add_subplot(111)
    p1=ax.text(37, 10, '$Foidite$', fontsize=20)
    p2=ax.text(41.5, 1, '$ Picro-$\n$basalt $', fontsize=20)
    p3=ax.text(47, 2.5, '$Basalt$', fontsize=20)
    p4=ax.text(55, 14, '$Phonolite$', fontsize=20)
    p5=ax.text(51, 11.5, '$Tephri-$\n$phonolite$', fontsize=20)
    p6=ax.text(52.3, 3, '$Basaltic$\n$Andesite$', fontsize=20)
    p7=ax.text(58, 3, '$Andesite$', fontsize=20)
    p8=ax.text(66, 5, '$Dacite$', fontsize=20)
    p9=ax.text(42, 6, '$Tephrite$\n$Basanite$', fontsize=20)
    p10=ax.text(47, 5.1, '$Tachy-$\n$basalt$', fontsize=20)
    p11=ax.text(47, 9, '$Phono-$\n$tephrite$', fontsize=20)
    p12=ax.text(50.7, 6.1, '$Basaltic$\n$trachy-$\n$andesite$', fontsize=20)
    p13=ax.text(56, 8, '$Trachy-$\n$andesite$', fontsize=20)
    p14=ax.text(62, 12, '$Trachyte$', fontsize=20)
    p15=ax.text(62.5, 8.5, '$Trachydacite$', fontsize=20)
    p16=ax.text(70, 8.7, '$Rhyolite$', fontsize=20)
    #Verticales
    plt.plot([41,41],[0,7],color='black')
    plt.plot([45,45],[0,5],color='black')
    plt.plot([52,52],[0,5],color='black')
    plt.plot([57,57],[0,5.9],color='black')
    plt.plot([63,63],[0,7],color='black')
    plt.plot([69,69],[8,13],color='black')
    #horizontales
    plt.plot([41,45],[3,3],color='black')
    plt.plot([45,52],[5,5],color='black')
    #Nor-Este
    plt.plot([41,52.5],[7,14],color='black')
    plt.plot([45,62.88235294],[5,14.5],color='black')
    plt.plot([52,69],[5,8],color='black')
    #Nor-Oeste
    plt.plot([69,77],[8,0],color='black')
    plt.plot([52,49.4],[5,7.3],color='black')
    plt.plot([49.4,45],[7.3,9.4],color='black')
    plt.plot([57,53],[5.9,9.3],color='black')
    plt.plot([48.4,53],[11.5,9.3],color='black')
    plt.plot([50.2826087,57.6],[15,11.7],color='black')
    plt.plot([57.6,63],[11.7,7],color='black')
    plt.xlabel('$SiO_{2}\ (wt\%)$',fontsize=20)
    plt.ylabel('$K_{2}O+Na_{2}O$\n$(wt\%) $',fontsize=20)
    plt.xlim(35, 80)
    plt.ylim(0,16)
    plt.title('TAS diagram. Lemaitre',fontsize=25)
    #ejemplo
    x=[50,60,70,45]
    y=[8,9,10,11]
    p1=plt.scatter(x,y,s=500,alpha=0.5,color='g',marker='D')
    plt.legend([p1, p2,p3], ["Caribbean-Colombia Plateau "])
    plt.savefig('TAS_Wii.jpg')
TAS()