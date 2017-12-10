import matplotlib.pyplot as plt
import numpy as np
X=(7.5,4.48,8.6,7.73,5.28,4.25,6.99,6.31,9.15,5.06)
Y=(28.66,20.37,22.33,26.35,22.29,21.74,23.11,23.13,24.68,21.89)

x=np.array([7.5,4.48,8.6,7.73,5.28,4.25,6.99,6.31,9.15,5.06])
y=np.array([28.66,20.37,22.33,26.35,22.29,21.74,23.11,23.13,24.68,21.89])
p=np.poly1d(np.polyfit(x,y,1))
p2=np.poly1d(np.polyfit(x,y,2))
p3=np.poly1d(np.polyfit(x,y,3))

xp=np.linspace(4,10)

fig, ax = plt.subplots()

ax.scatter(X,Y)
ax.title("Regresión con poli de 1 2 y 3° grado")
ax.plot(xp,p2(xp),"-",label="p2")
ax.plot(xp,p3(xp),"--",label="p3")
ax.plot(xp,p(xp),"o",label="p1")
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.ylabel('X', fontsize = 16)
plt.xlabel('Y', fontsize = 16)
plt.show()

