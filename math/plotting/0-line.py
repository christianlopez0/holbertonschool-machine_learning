#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def line():
    y = np.arange(0, 11) ** 3  # y = x^3 for x in [0, 10]
    x = np.arange(0, 11)       # x values from 0 to 10

    # Plot the graph with a solid red line
    plt.plot(x, y, 'r-', lw=2)  # 'r-' specifies red color and solid line; lw=2 for line width

    # Set the x-axis range from 0 to 10
    plt.xlim(0, 11)

    # Set the y-axis range to fit the cubic values
    plt.ylim(0, 1001)  # Since y = x^3, the maximum y value is 10^3 = 1000

    # Remove grid and extra labels to match the reference exactly
    plt.grid(False)

    # Display the plot
    plt.show()
