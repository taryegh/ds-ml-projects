""""
He throws a dice 100 times.
If its 1 or 2, he goes one step down.
If its 3, 4, or 5 he goes one step up.
If its 6, he will throw the dice again and will walk up by the resulting number of steps.
There is a 0.1% chance of falling down the stairs when he makes a move. Falling down means he should start from step 0.
He bets he will reach step 60.
Calculating the odds...
"""

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

all_walks = []
for i in range(1000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

aw = np.array(all_walks)

np_aw_t = np.transpose(aw)
plt.plot(np_aw_t)
plt.show()

plt.cla()

ends = np_aw_t[-1, :]
plt.hist(ends)
plt.show()

odds = np.mean(ends >= 60)
print(odds)
