#Dependencies
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Denife Lorenz Ecuations System
def lorenz(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Set parameters for the Lorenz system
sigma = 10.0
rho = 28.0
beta = 5

# Initial conditions: Beacuse its a chaotic system the initial conditions generate different results
x0, y0, z0 = 0.1, 0.0, 0.0
xyz0 = [x0, y0, z0]

# Time Inverval
t_span = (0, 100)
t_eval = np.linspace(0, 100, 10000)  #Time Vector For Evaluation


# Resolve differential Lorenz equations using Runge-Kutta of 4th and 5th order
sol = solve_ivp(lorenz, t_span, xyz0, args=(sigma, rho, beta), t_eval=t_eval)


# Print the first 3 solutions
x, y, z = sol.y

print("First 3 solutions:")
print("x:", x[:20])
print("y:", y[:3])
print("z:", z[:3])


# Plot Lorenz Attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Lorenz's Attractor")
plt.show()

