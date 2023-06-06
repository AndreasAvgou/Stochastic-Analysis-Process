import numpy as np
import matplotlib.pyplot as plt
import random
import csv
from statsmodels.graphics.tsaplots import plot_acf

def generate_random_values(size):
    return [round(random.uniform(-1.00, 1.00), 1) for _ in range(size)]

def generate_g_values(size):
    return generate_random_values(size)

def generate_w_values(size):
    return generate_random_values(size)

def generate_t_values(a, s, w):
    t = np.zeros(len(w))
    for i in range(1, len(w)):
        t[i] = -a * t[i-1] + s * w[i]
    return t

def generate_a_values(b, g):
    a = np.zeros(len(b))
    for i in range(len(b)):
        a[i] = b[i] * g[i] + 150
        a[i] = np.log(a[i])
        if np.isnan(a[i]):
            a[i] = 0
    return a

def generate_smoothed_values(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

def plot_and_save(data, filename, xlabel, ylabel, color='blue', smoothed=False):
    plt.plot(data, label='Original' if not smoothed else 'Smoothed', color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(filename, format='pdf')
    plt.show()

def main():
    np.random.seed(0)
    plt.rcParams["figure.figsize"] = (20, 15)

    size = 10000
    window_size = 30
    a = 0.8
    s1 = 30
    s2 = 120

    w1 = generate_w_values(size)
    w2 = generate_w_values(size)
    g1 = generate_g_values(size)
    g2 = generate_g_values(size)

    with open('OData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['w1', 'w2'])
        for i in range(size):
            writer.writerow([w1[i], w2[i]])

    t1 = generate_t_values(a, s1, w1)
    b1 = t1
    a1 = generate_a_values(b1, g1)
    smoothed_a1 = generate_smoothed_values(a1, window_size)
    plot_and_save(a1, 'a1.pdf', 'Time', 'Value')
    plot_and_save(smoothed_a1, 'smoothed_a1.pdf', 'Time', 'Value', color='red', smoothed=True)

    t2 = generate_t_values(a, s2, w2)
    b2 = t2
    a2 = generate_a_values(b2, g2)
    smoothed_a2 = generate_smoothed_values(a2, window_size)
    plot_and_save(a2, 'a2.pdf', 'Time', 'Value')
    plot_and_save(smoothed_a2, 'smoothed_a2.pdf', 'Time', 'Value', color='red', smoothed=True)

    diff1 = [a1[i] - a1[i-1] for i in range(1, len(a1))]
    diff2 = [a2[i] - a2[i-1] for i in range(1, len(a2))]
    smoothed_diff1 = generate_smoothed_values(diff1, window_size)
    smoothed_diff2 = generate_smoothed_values(diff2, window_size)
    plot_and_save(diff1, 'diff1.pdf', 'Time', 'Value')
    plot_and_save(smoothed_diff1, 'smoothed_diff1.pdf', 'Time', 'Value', color='red', smoothed=True)
    plot_and_save(diff2, 'diff2.pdf', 'Time', 'Value')
    plot_and_save(smoothed_diff2, 'smoothed_diff2.pdf', 'Time', 'Value', color='red', smoothed=True)

    plot_acf(a1, lags=100)
    plt.savefig('autoc1.pdf', format='pdf')
    plt.show()

    plot_acf(smoothed_a1, lags=100)
    plt.savefig('auto1.pdf', format='pdf')
    plt.show()

    plot_acf(a2, lags=100)
    plt.savefig('autoc2.pdf', format='pdf')
    plt.show()

    plot_acf(smoothed_a2, lags=100)
    plt.savefig('auto2.pdf', format='pdf')
    plt.show()

if __name__ == '__main__':
    main()

