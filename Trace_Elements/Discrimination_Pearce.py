import matplotlib.pyplot as plt

#This program plot trace elements of your data according to 
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(221)

p1=ax.text(25, 2000, 'Within-plate \ngranite', fontsize=12)
p2=ax.text(41.5, 25, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=12)
p3=ax.text(100, 5, 'Ocean ridge granite', fontsize=12)
p4=ax.text(2, 10, 'Volcanic arc and syn- \ncollision granites', fontsize=12)

ax.plot([1,50],[2000,10],color='black')
ax.plot([50,40],[10,1],color='black')
ax.plot([50,1000],[10,100],color='black')
ax.plot([25,1000],[25,400],color='black')

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('Y (ppm)',fontsize=12)
ax.set_ylabel('Nb (ppm)',fontsize=12)
ax.set_xlim(1, 1000)
ax.set_ylim(1,10000)

#DATOS BATOLITO
x=[12.76,14.105,20.834,15.924,16.346,24.465]
y=[8.741,8.251,6.426,6.067,6.297,9.055]

p1= ax.scatter(x,y,s=500,alpha=0.75,color='r')

#segundo

ax2 = fig.add_subplot(222)

p11=ax2.text(25, 2000, 'Within-plate \ngranite', fontsize=12)
p22=ax2.text(41.5, 25, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=12)
p33=ax2.text(100, 5, 'Ocean ridge granite', fontsize=12)
p44=ax2.text(2, 10, 'Volcanic arc and syn- \ncollision granites', fontsize=12)



ax2.plot([1,50],[2000,10],color='black')
ax2.plot([50,40],[10,1],color='black')
ax2.plot([50,1000],[10,100],color='black')
ax2.plot([25,1000],[25,400],color='black')

ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_xlabel('Y (ppm)',fontsize=12)
ax2.set_ylabel('Nb (ppm)',fontsize=12)
ax2.set_xlim(1, 1000)
ax2.set_ylim(1,10000)


p111= ax2.scatter(x,y,s=500,alpha=0.75,color='r')

#tercero

ax3 = fig.add_subplot(223)

p111=ax3.text(25, 2000, 'Within-plate \ngranite', fontsize=12)
p222=ax3.text(41.5, 25, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=12)
p333=ax3.text(100, 5, 'Ocean ridge granite', fontsize=12)
p444=ax3.text(2, 10, 'Volcanic arc and syn- \ncollision granites', fontsize=12)



ax3.plot([1,50],[2000,10],color='black')
ax3.plot([50,40],[10,1],color='black')
ax3.plot([50,1000],[10,100],color='black')
ax3.plot([25,1000],[25,400],color='black')

ax3.set_yscale('log')
ax3.set_xscale('log')
ax3.set_xlabel('Y (ppm)',fontsize=12)
ax3.set_ylabel('Nb (ppm)',fontsize=12)
ax3.set_xlim(1, 1000)
ax3.set_ylim(1,10000)


p1111= ax3.scatter(x,y,s=500,alpha=0.75,color='r')



ax4 = fig.add_subplot(224)

p1111=ax4.text(25, 2000, 'Within-plate \ngranite', fontsize=12)
p2222=ax4.text(41.5, 25, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=12)
p3333=ax4.text(100, 5, 'Ocean ridge granite', fontsize=12)
p4444=ax4.text(2, 10, 'Volcanic arc and syn- \ncollision granites', fontsize=12)



ax4.plot([1,50],[2000,10],color='black')
ax4.plot([50,40],[10,1],color='black')
ax4.plot([50,1000],[10,100],color='black')
ax4.plot([25,1000],[25,400],color='black')

ax4.set_yscale('log')
ax4.set_xscale('log')
ax4.set_xlabel('Y (ppm)',fontsize=12)
ax4.set_ylabel('Nb (ppm)',fontsize=12)
ax4.set_xlim(1, 1000)
ax4.set_ylim(1,10000)


p11111= ax4.scatter(x,y,s=500,alpha=0.75,color='r')


fig.savefig('Nb_Y_Pearce.tif', format='tif', dpi=500)
