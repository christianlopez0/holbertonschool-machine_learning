#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def line():
    y = np.arange(0, 11) ** 3  # y = x^3 for x in [0, 10]
    x = np.arange(0, 11)       # x values from 0 to 10

    plt.figure(figsize=(6.4, 4.8))

    # Plot y as a solid red line
    plt.plot(x, y, 'r-', label='y = x^3')

    # Set x-axis range from 0 to 10
    plt.xlim(0, 10)

    # Ensure the y-axis also adjusts according to the cubic values
    plt.ylim(min(y), max(y))

    # Add title and labels
    plt.title('y = x^3')
    plt.xlabel('x')
    plt.ylabel('y')

    # Show the plot
    plt.show()
