#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """Plot the exponential decay of C-14 with logarithmic scale on y-axis."""
    
    x = np.arange(0, 28651, 5730)  # Time points from 0 to 28650, step size 5730
    t = 5730  # Half-life of C-14 in years
    y = 0.5**(x / t)  # Exponential decay function (Fraction Remaining)

    plt.figure(figsize=(6.4, 4.8))

    # Plot the data as a line graph
    plt.plot(x, y)

    # Set the title and axis labels
    plt.title("Exponential Decay of C-14")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    # Set the y-axis to a logarithmic scale
    plt.yscale("log")

    # Set the x-axis range from 0 to 28650
    plt.xlim(0, 28650)

    # Show the plot
    plt.show()
