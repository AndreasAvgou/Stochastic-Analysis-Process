import numpy as np
import matplotlib.pyplot as plt
import random
import csv

def generate_random_data(size):
    w1 = np.zeros(size)
    w2 = np.zeros(size)
    a = np.zeros(size)
    for i in range(size):
        w1[i] = round(random.uniform(-1.00, 1.00), 1)
        w2[i] = round(random.uniform(-1.00, 1.00), 1)
        a[i] = round(random.uniform(-1.00, 1.00), 1)
    return w1, w2, a

def write_data_to_csv(filename, w1, w2, a):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2', 'a'])
        for i in range(len(w1)):
            writer.writerow([w1[i], w2[i], a[i]])

def apply_smoothing_moving_average(original_series, window_size):
    smoothed_series = np.convolve(original_series, np.ones(window_size) / window_size, mode='valid')
    return smoothed_series

# Generate random data
size = 1000
w1, w2, a = generate_random_data(size)

# Write the generated data to a CSV file
write_data_to_csv('OData.csv', w1, w2, a)

# Apply smoothing moving average to t1
window_size = 3  # Adjust the window size as needed
t1 = np.zeros(size)
t2 = np.zeros(size)
s1 = 2
s2 = 120

t1[0] = 1
for i in range(1, size):
    if i != 0:
        t1[i] = -a[i] * t1[i-1] + s1 * w1[i]

# Smooth t1 using moving average
smoothed_t1 = apply_smoothing_moving_average(t1, window_size)

# Plotting the original and smoothed series for t1
plt.figure(figsize=(20, 12))
plt.plot(t1, label='Original t1')
plt.plot(smoothed_t1, label='Smoothed t1')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate differences for t1
diff1 = [t1[i] - t1[i-1] for i in range(1, len(t1))]

t2[0] = 1
for i in range(1, size):
    if i != 0:
        t2[i] = -a[i] * t2[i-1] + s2 * w2[i]

# Smooth t2 using moving average
smoothed_t2 = apply_smoothing_moving_average(t2, window_size)

# Plotting the original and smoothed series for t2
plt.figure(figsize=(20, 12))
plt.plot(t2, label='Original t2')
plt.plot(smoothed_t2, label='Smoothed t2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate differences for t2
diff2 = [t2[i] - t2[i-1] for i in range(1, len(t2))]

# Smooth the differences using moving average
smoothed_diff1 = apply_smoothing_moving_average(diff1, window_size)
smoothed_diff2 = apply_smoothing_moving_average(diff2, window_size)

# Plotting the original and smoothed differences for t1
plt.figure(figsize=(20, 12))
plt.plot(diff1, label='Original diff1')
plt.plot(smoothed_diff1, label='Smoothed diff1')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
# Plotting the original and smoothed differences for t2
plt.figure(figsize=(20, 12))
plt.plot(diff2, label='Original diff2')
plt.plot(smoothed_diff2, label='Smoothed diff2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
