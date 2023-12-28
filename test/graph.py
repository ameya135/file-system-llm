import matplotlib.pyplot as plt
import numpy as np

# Enable inline plotting for Jupyter notebook
%matplotlib inline

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Sinusoidal Plot')

# Show the plot
plt.show()
