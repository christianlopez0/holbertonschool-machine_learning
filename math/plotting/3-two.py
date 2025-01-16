#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def two():
    """Plot exponential decay for two radioactive elements (C-14 and Ra-226)."""
    
    x = np.arange(0, 21001, 1000)  # Time points from 0 to 20,000, step size 1000
    r = np.log(0.5)
    t1 = 5730  # Half-life of C-14 in years
    t2 = 1600  # Half-life of Ra-226 in years
    y1 = np.exp((r / t1) * x)  # Exponential decay for C-14
    y2 = np.exp((r / t2) * x)  # Exponential decay for Ra-226
    
    plt.figure(figsize=(6.4, 4.8))

    # Plot the data as line graphs
    plt.plot(x, y1, 'r--', label="C-14")  # Dashed red line for C-14
    plt.plot(x, y2, 'g-', label="Ra-226")  # Solid green line for Ra-226

    # Set the title and axis labels
    plt.title("Exponential Decay of Radioactive Elements")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    # Set the x-axis and y-axis range
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # Add a legend in the upper right corner
    plt.legend(loc="upper right")

    # Show the plot
    plt.show()
