import numpy as np
import matplotlib.pyplot as plt
import random
import csv

def generate_random_data(size):
    w1 = np.zeros(size)
    w2 = np.zeros(size)
    for i in range(size):
        w1[i] = round(random.uniform(-1.0, 1.0), 1)
        w2[i] = round(random.uniform(-1.0, 1.0), 1)
    return w1, w2

def write_data_to_csv(filename, w1, w2):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2'])
        for i in range(len(w1)):
            writer.writerow([w1[i], w2[i]])

# Generate random data
size = 1000
w1, w2 = generate_random_data(size)

# Write the generated data to a CSV file
write_data_to_csv('OData.csv', w1, w2)

# Apply smoothing moving average to t1
t1 = np.zeros(size)
t2 = np.zeros(size)
s1 = 2
s2 = 120

for i in range(1, size):
    t1[i] = t1[i-1] + s1 * np.sqrt(1 / size) * w1[i]

# Plotting the original series for t1
plt.figure(figsize=(20, 12))
plt.plot(t1, label='Original t1')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate differences for t1
diff1 = [t1[i] - t1[i-1] for i in range(1, len(t1))]

for i in range(1, size):
    t2[i] = t2[i-1] + s2 * np.sqrt(1 / size) * w2[i]

# Plotting the original series for t2
plt.figure(figsize=(20, 12))
plt.plot(t2, label='Original t2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate differences for t2
diff2 = [t2[i] - t2[i-1] for i in range(1, len(t2))]

# Plotting the original differences for t1
plt.figure(figsize=(20, 12))
plt.plot(diff1, label='Original diff1')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# Plotting the original differences for t2
plt.figure(figsize=(20, 12))
plt.plot(diff2, label='Original diff2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
