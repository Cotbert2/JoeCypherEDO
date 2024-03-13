import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class Lorenz:
    def __init__(self, beta):
        self.sigma = 10.0
        self.rho = 28.0
        self.beta = beta
        self.x0 = 0.1
        self.y0 = 0.0
        self.z0 = 0.0
        self.xyz0 = [0.1, 0.0, 0.0]
        self.t_span = (0, 100)
        self.t_eval = np.linspace(0, 100, 10000)

    def lorenzBuilder(self, t, xyz):
        x, y, z = xyz
        dxdt = self.sigma * (y - x)
        dydt = x * (self.rho - z) - y
        dzdt = x * y - self.beta * z
        return [dxdt, dydt, dzdt]
    

    def solve_lorenz(self):
        sol = solve_ivp(self.lorenzBuilder, self.t_span, self.xyz0,  t_eval=self.t_eval)
        x, y, z = sol.y
        return x, y, z

    def print_first_3_solutions(self):
        x, y, z = self.solve_lorenz()
        print("First 3 solutions:")
        print("x:", x[70])
        print("y:", y[:3])
        print("z:", z[:3])

    def draw_attractor(self):
        x, y, z = self.solve_lorenz()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, linewidth=0.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Atractor de Lorenz')
        plt.show()

    def getPosition(self, axis, position):
        x , y, z = self.solve_lorenz()
        if axis == "x":
            return round(x[position],2)
        elif axis == "y":
            return round(y[position],2)
        elif axis == "z":
            return round(z[position],2)
        else:
            return "Invalid axis"
