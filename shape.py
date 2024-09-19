import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define control points (closing the loop by repeating the first point)
control_points = np.array([[0, 0], [1, 2], [3, 3], [3, 1], [0, 0]])  # Closing by repeating the first point
x, y = control_points[:, 0], control_points[:, 1]

# Parameter t for each control point
t_control = np.linspace(0, 1, len(control_points))

# Create cubic splines for both x and y with periodic boundary conditions
cs_x = CubicSpline(t_control, x, bc_type='periodic')
cs_y = CubicSpline(t_control, y, bc_type='periodic')

# Generate new parameter t for smooth interpolation
t_new = np.linspace(0, 1, 100)

# Get the spline values for x and y
spline_x = cs_x(t_new)
spline_y = cs_y(t_new)

# Plot
plt.plot(spline_x, spline_y, label='Closed Cubic Spline')
plt.scatter(x, y, color='red', label='Control Points')
plt.legend()
plt.title('Closed Cubic Spline Parameterization')
plt.axis('equal')
plt.show()
