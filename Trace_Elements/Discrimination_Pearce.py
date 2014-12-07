

#This program plots your own trace element data based on: Pearce, J.A., Harris, N.B.W., and Tindle, A.G., 1984, Trace element discrimination diagrams for the tectonic interpretation of granitic rocks:  Journal of Petrology, v. 25, p. 956-983.


import matplotlib.pyplot as plt

#the size of the graph is established as 12, 10
fig = plt.figure(figsize=(12,10))

#First subplot: Nb vs Y diagram

NbY = fig.add_subplot(221)

#Text of the fields in the Nb VS Y diagram
T_NbY1=NbY.text(25, 2000, 'Within-plate \ngranite', fontsize=12)
T_NbY2=NbY.text(41.5, 25, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=12)
T_NbY3=NbY.text(100, 5, 'Ocean ridge granite', fontsize=12)
T_NbY4=NbY.text(2, 10, 'Volcanic arc and syn- \ncollision granites', fontsize=12)

#Plot of the field divisions
NbY.plot([1,50],[2000,10],color='black')
NbY.plot([50,40],[10,1],color='black')
NbY.plot([50,1000],[10,100],color='black')
NbY.plot([25,1000],[25,400],color='black')

#Log scale
NbY.set_yscale('log')
NbY.set_xscale('log')

#labels and limits of the diagram
NbY.set_xlabel('Y (ppm)',fontsize=12)
NbY.set_ylabel('Nb (ppm)',fontsize=12)
NbY.set_xlim(1, 1000)
NbY.set_ylim(1,10000)

#DATOS BATOLITO
x=[12.76,14.105,20.834,15.924,16.346,24.465]
y=[8.741,8.251,6.426,6.067,6.297,9.055]

plot_NbY= NbY.scatter(x,y,s=500,alpha=0.75,color='r')

"
#Second subplot: Ta vs Yb

TaYb = fig.add_subplot(222)

T_TaYb1=TaYb.text(5, 50, 'Within-plate \ngranite', fontsize=12)
T_TaYb2=TaYb.text(0.2, 5, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=12)
T_TaYb3=TaYb.text(10, 5, 'Ocean ridge granite', fontsize=12)
T_TaYb4=TaYb.text(1, 0.1, 'Volcanic arc and syn- \ncollision granites', fontsize=12)



TaYb.plot([0.55,3],[20,2],color='black')
TaYb.plot([3,100],[2,20],color='black')
TaYb.plot([3,0.1],[2,0.35],color='black')
TaYb.plot([5,5],[1,0.05],color='black')
TaYb.plot([5,100],[1,0.7],color='black')
TaYb.plot([3,5],[2,1],color='black'

TaYb.set_yscale('log')
TaYb.set_xscale('log')

TaYb.set_xlabel('Yb (ppm)',fontsize=12)
TaYb.set_ylabel('Ta (ppm)',fontsize=12)
TaYb.set_xlim(0.1, 100)
TaYb.set_ylim(0.01,100)


plot_TaYb= TaYb.scatter(x,y,s=500,alpha=0.75,color='r')
"
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
