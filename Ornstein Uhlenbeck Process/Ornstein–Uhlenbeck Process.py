# Required libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import csv
from statsmodels.graphics.tsaplots import plot_acf

# Ornstein-Uhlenbeck process
# Stochastic differential equation: dxt/dt = -axtdt + σ*Wdt

# Initialize t1,t2
t1 = np.zeros(1000)
t2 = np.zeros(1000)
s1 = 30
s2 = 120

# Initialize w1,w2, and a and import 1000 random values between -1 and 1
w1 = np.zeros(1000)
w2 = np.zeros(1000)
a = np.zeros(1000)

for i in range(1000):
    w1[i] = round(random.uniform(-1.00,1.00),1)
    w2[i] = round(random.uniform(-1.00,1.00),1)
    a[i] = round(random.uniform(-1.00,1.00),1)

# Save w1, w2, and a values to a .csv file
with open('OData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['w1', 'w2', 'a'])
    for i in range(1000):
        writer.writerow([w1[i], w2[i], a[i]])

# Apply the equation for the w values and with t value and s1 = 30
# dxt/dt = -axtdt + σ*Wdt

t1[0] = 1
for i in range(1,1000):
    if i != 0 :
        t1[i] = -a[i]*t1[i-1] + s1*w1[i]

# Plot the results of the equation for σ = 30 and their respective difference
plt.plot(t1)
diff1 = [t1[i] - t1[i-1] for i in range(1,len(t1))]
plt.plot(diff1)
plt.show()
# Apply the equation for the w values and with t value and s2 = 120
# dxt/dt = -axtdt + σ*Wt

t2[0] = 1
for i in range(1,1000):
    if i != 0 :
        t2[i] = -a[i]*t2[i-1] + s2*w2[i]

# Plot the results of the equation for σ = 120 and their respective difference
plt.plot(t2)
diff2 = [t2[i] - t2[i-1] for i in range(1,len(t2))]
plt.plot(diff2)
plt.show()
# Plot the results of the equation with autocorrelation
plot_acf(t1,lags=500)
plt.show()
plot_acf(t2,lags=500)
plt.show()

