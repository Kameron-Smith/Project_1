import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3.5, 3.5, 0.01)
def f(x):
    return (x-3)*(x+3)*(x-4)*(x+4)*(x-1)*(x-2)*(x+2)/350 
y_true = f(x)
n_x = len(x)
plt.plot(x, y_true)
plt.show()

