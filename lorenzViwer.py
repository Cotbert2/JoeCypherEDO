#Depedencias: numpy, matplotlib, scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definir las ecuaciones de Lorenz
def lorenz(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parámetros de las ecuaciones de Lorenz
sigma = 10.0
rho = 28.0
beta = 5

# Condiciones iniciales
x0, y0, z0 = 0.1, 0.0, 0.0
xyz0 = [x0, y0, z0]

# Intervalo de tiempo
t_span = (0, 100)
t_eval = np.linspace(0, 100, 10000)  # Vector de tiempo para la evaluación

# Resolver las ecuaciones de Lorenz utilizando Runge-Kutta de cuarto y quinto orden
sol = solve_ivp(lorenz, t_span, xyz0, args=(sigma, rho, beta), t_eval=t_eval)




# Extraer las soluciones
x, y, z = sol.y

print("First 3 solutions:")
print("x:", x[:20])
print("y:", y[:3])
print("z:", z[:3])


# Visualizar el atractor de Lorenz
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Atractor de Lorenz')
plt.show()

