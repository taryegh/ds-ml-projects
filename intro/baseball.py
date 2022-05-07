import numpy as np
import math
#import sys
#np.set_printoptions(threshold=sys.maxsize)

# Generating sample data via Laplace–Gauss probability Normal Distribution
height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60, 10, 5000), 1)


# np arrays
np_height = np.array(height)
np_weight = np.array(weight)

# convert to meters
np_heigh_m = np_height * 0.0254
np_weight_kg = np_weight * 0.453592


# bmi
bmi = np_weight / np_height ** 2

# people with light weight
light = np.array(bmi < 21) #true/false
print(light)
print(bmi[light])

# subset
print(np_height[100:111])

# 2d arrays
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)

# creating np_city column stack array from height and wieght
np_city = np.column_stack((height, weight))
#printing the 51th row
print(np_city[50, :])
#printing the entire column
print(np_city[:, 1])
#printing height if 120th player
print(np_city[119, 0])

np_upd_height = np.random.normal(1.5, 0.5, 5000)
np_upd_weight = np.random.normal(40, 5, 5000)
np_comp_upd = np.column_stack((np_upd_height, np_upd_weight))
np_final_city = np_city + np_comp_upd
print(np_final_city)

# basic statistics
print(np.mean(np_height))
print(np.median(np_height))
stdev_np_city = np.std(np_city[:, 0])
print((stdev_np_city))
print("Standard Deviation: " + str(stdev_np_city))
