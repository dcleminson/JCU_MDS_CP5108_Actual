import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

###########################################################
#   TASK: Week6 Book 4 Task 1
###########################################################
print(f'\nWeek6 Book 4 Task 1\n')
my_data1 = np.array([43, 37, 94, 64, 89, 57, 12, 32, 98, 74, 39, 56, 91, 61, 53, 36, 94, 34, 23, 62, 59, 92, 85, 86, 52])
plt.plot(my_data1)
plt.show()

###########################################################
#   TASK: Week6 Book 4 Task 2
###########################################################
print(f'\nWeek6 Book 4 Task 2\n')
my_data2 = pd.DataFrame(np.random.randint(0,100,size=(20, 4)), columns=list('ABCD'))
my_data2.plot.hist(bins=4)
plt.show()

###########################################################
#   TASK: Week6 Book 4 Task 3
###########################################################
print(f'\nWeek6 Book 4 Task 3\n')
my_data2.plot.hist(bins=4, subplots=True)
plt.show()