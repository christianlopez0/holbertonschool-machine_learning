#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def scatter():
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # Plot the data as a scatter plot with magenta points
    plt.scatter(x, y, color='magenta')

    # Set the title and axis labels
    plt.title("Men's Height vs Weight")
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')

    # Show the plot
    plt.show()
