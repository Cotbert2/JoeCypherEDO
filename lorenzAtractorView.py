import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation

a = 10
b = 28
c = 8/3

tf=50
N=10**4
h=tf/N

t=np.linspace(0,tf,N)
x = [0.1]
y = [0]
z = [0]

def f(x,y,z):
  return a*(y-x)

def g(x,y,z):
  return x*(b-z)-y

def j(x,y,z):
  return x*y-c*z

for n in range(N-1):
  kx1 = f(x[n],y[n],z[n])
  ky1 = g(x[n],y[n],z[n])
  kz1 = j(x[n],y[n],z[n])
  kx2 = f(x[n] + h*kx1/2,y[n] + h*ky1/2,z[n] + h*kz1/2)
  ky2 = g(x[n] + h*kx1/2,y[n] + h*ky1/2,z[n] + h*kz1/2)
  kz2 = j(x[n] + h*kx1/2,y[n] + h*ky1/2,z[n] + h*kz1/2)
  kx3 = f(x[n] + h*kx2/2,y[n] + h*ky2/2,z[n] + h*kz2/2)
  ky3 = g(x[n] + h*kx2/2,y[n] + h*ky2/2,z[n] + h*kz2/2)
  kz3 = j(x[n] + h*kx2/2,y[n] + h*ky2/2,z[n] + h*kz2/2)
  kx4 = f(x[n] + h*kx3,y[n] + h*ky3,z[n] + h*kz3)
  ky4 = g(x[n] + h*kx3,y[n] + h*ky3,z[n] + h*kz3)
  kz4 = j(x[n] + h*kx3,y[n] + h*ky3,z[n] + h*kz3)

  x.append(x[n]+(h/6)*(kx1 + 2*kx2 + 2*kx3 + kx4))
  y.append(y[n]+(h/6)*(ky1 + 2*ky2 + 2*ky3 + ky4))
  z.append(z[n]+(h/6)*(kz1 + 2*kz2 + 2*kz3 + kz4))

plt.plot(x,z)
plt.title("Atractor de Lorenz")
plt.xlabel("x")
plt.ylabel("z")
plt.show()

fig=plt.figure()
ax=fig.gca()

def actualizar(i):
  ax.clear()

  ax.plot(x[:i], z[:i],'-')
  ax.set_title("Atractor de Lorenz")
  ax.plot(x[i],  z[i],'o',markersize=10,color='r')