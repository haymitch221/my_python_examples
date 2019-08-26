import matplotlib.pyplot as mp
import numpy as np

x = np.arange(0, 3* np.pi, 0.1)

y = np.sin(x)

mp.plot(x, y)
mp.plot(x, np.cos(y))

mp.show()