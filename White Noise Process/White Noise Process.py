import numpy as np
import matplotlib.pyplot as plt
import random
import csv
from statsmodels.graphics.tsaplots import plot_acf

t1 = np.zeros(1000)
t2 = np.zeros(1000)
w = np.zeros(1000)
s1 = 30
s2 = 120

# Initialize t1,t2,w and add 1000 random values between -1 and 1
for i in range(1000):
    t1[i] = round(random.uniform(-1.00, 1.00), 1)
    t2[i] = round(random.uniform(-1.00, 1.00), 1)
    w[i] = round(random.uniform(-1.00, 1.00), 1)

# Save the values of w to a .csv file
with open('WData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['w'])
    for i in range(1000):
        writer.writerow([w[i]])

# Compute the values of t1,t2 using the formula t[i] = t[i-1] + a*w[i]
t1[0] = 1
t2[0] = 1
for i in range(1, 1000):
    t1[i] = t1[i-1] + s1*w[i]
    t2[i] = t2[i-1] + s2*w[i]

# Plot the values of t
plt.plot(t1)
plt.title('t1 values')
plt.xlabel('Index')
plt.ylabel('Value')
plt.plot(t2)
plt.title('t2 values')
plt.xlabel('Index')
plt.ylabel('Value')

# Compute the differences between successive values of t and plot them
diff1 = [t1[i] - t1[i-1] for i in range(1, len(t1))]
diff2 = [t2[i] - t2[i-1] for i in range(1, len(t2))]
plt.figure()
plt.plot(diff1)
plt.title('Differences between successive t1 values')
plt.xlabel('Index')
plt.ylabel('Value')
plt.plot(diff2)
plt.title('Differences between successive t2 values')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
