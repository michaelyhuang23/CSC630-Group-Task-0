import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(17)
y = np.random.randn(17)

x2 = np.random.randn(78)
y2 = np.random.randn(78)

plt.scatter(x, y, color='#FF0000', label='17 Points')
plt.scatter(x2, y2, color='#0000FF', label='78 Points')
plt.legend()
plt.savefig('scatter_plot.png')