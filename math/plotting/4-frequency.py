#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of student grades for Project A."""
    
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    
    plt.figure(figsize=(6.4, 4.8))
    
    # Plot the histogram with bins every 10 units
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    
    # Set the title and axis labels
    plt.title("Project A")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    
    # Show the plot
    plt.show()
