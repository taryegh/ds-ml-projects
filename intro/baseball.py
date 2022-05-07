import numpy as np
import math
import sys
np.set_printoptions(threshold=sys.maxsize)

# Generating sample data via Laplace–Gauss probability Normal Distribution
height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60, 10, 5000), 1)



st_dev = np.std(height)
