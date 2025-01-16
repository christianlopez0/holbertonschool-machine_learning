#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def change_scale():
    x = np.arange(0, 28651, 5730)  # Time points from 0 to 28650, step size of 5730
    r = np.log(0.5)  # Natural log of 0.5 (decay factor for C-14)
    t = 5730  # Half-life of C-14 in years
    y = np.exp((r / t) * x)  # Exponential decay formula

    plt.figure(figsize=(6.4, 4.8))

    # Plot the data as a line graph
    plt.plot(x, y)

    # Set the title and axis labels
    plt.title("Exponential Decay of C-14")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    # Set the y-axis to a logarithmic scale
    plt.yscale("log")

    # Show the plot
    plt.show()
