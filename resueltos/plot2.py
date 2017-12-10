import matplotlib.pyplot as plt
import numpy as np
def f(x):
	return x**3+x**2-4*x+4
 
def f1(x):
	return 3*x**2+2*x-4
	
x=np.arange(-10,10,0.1)

plt.plot(x,[f(i) for i in x],label="f(x)")
plt.plot(x,[f1(i) for i in x],label="f'(x)")
plt.xlabel("X")
plt.ylabel("Y")

plt.title("graf de la funcion y su derivada")
plt.legend()
plt.show()