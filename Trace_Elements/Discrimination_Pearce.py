import matplotlib.pyplot as plt


fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)

p1=ax.text(25, 2000, 'Within-plate \ngranite', fontsize=20)
p2=ax.text(41.5, 25, ' Within-plate granite and \nMORB anomalous ridge \nsegments', fontsize=20)
p3=ax.text(100, 5, 'Ocean ridge granite', fontsize=20)
p4=ax.text(2, 10, 'Volcanic arc and syn- \ncollision granites', fontsize=20)



plt.plot([1,50],[2000,10],color='black')
plt.plot([50,40],[10,1],color='black')
plt.plot([50,1000],[10,100],color='black')
plt.plot([25,1000],[25,400],color='black')

plt.yscale('log')
plt.xscale('log')
plt.xlabel('Y (ppm)',fontsize=20)
plt.ylabel('Nb (ppm)',fontsize=20)
plt.xlim(1, 1000)
plt.ylim(1,10000)
plt.title('Nb vs Y discrimination diagram for the tectonic \ninterpretation of granitic rocks (Pearce,1984)',fontsize=25)

#DATOS BATOLITO
x=[12.76,14.105,20.834,15.924,16.346,24.465]
y=[8.741,8.251,6.426,6.067,6.297,9.055]

p1= plt.scatter(x,y,s=500,alpha=0.75,color='r')
plt.legend([p1, p2,p3], ["Ibague Batholith "])
fig.savefig('Nb_Y_Pearce.tif', format='tif', dpi=1000)
