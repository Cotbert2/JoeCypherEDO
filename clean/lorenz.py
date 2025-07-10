import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class Lorenz:
    def __init__(self, beta):
        self.sigma = 10.0
        self.rho = 28.0
        self.beta = beta
        self.xyz0 = [0.1, 0.0, 0.0]
        self.t_span = (0, 100)
        self.t_eval = np.linspace(0, 100, 10000)
        self.x , self.y , self.z = self.solve_lorenz()

    def lorenz_builder(self, t, xyz):
        x, y, z = xyz
        dxdt = self.sigma * (y - x)
        dydt = x * (self.rho - z) - y
        dzdt = x * y - self.beta * z
        return [dxdt, dydt, dzdt]

    def solve_lorenz(self):
        sol = solve_ivp(self.lorenz_builder, self.t_span, self.xyz0,  t_eval=self.t_eval)
        x, y, z = sol.y
        return x, y, z

    def draw_attractor(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.x, self.y, self.z, linewidth=0.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f"x={self.beta}")
        plt.show()

    def get_position(self, axis, position):
        if axis == "x":
            return round(self.x[position],2)
        elif axis == "y":
            return round(self.y[position],2)
        elif axis == "z":
            return round(self.z[position],2)
        else:
            return "Invalid axis"
