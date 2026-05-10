"""
CPSC 250L
Lab 2: Python Review and Git Fundamentals

This program reads temperature data from a text file and computes
basic statistics.

Complete the TODO sections below.
"""

from pathlib import Path
import matplotlib.pyplot as plt


def read_temperatures(filename):
    """
    Read temperature values from a text file.

    Each line of the file should contain one number.

    Parameters
    ----------
    filename : str or Path
        Path to the input data file.

    Returns
    -------
    list of float
        Temperature values read from the file.
    """
    temperatures = []

    # TODO: Open the file and read each line.
    f = open(filename, "r")
    # TODO: Convert each non-blank line to a float.
    # TODO: Append each temperature to the temperatures list.
    for line in f:
        temperatures.append(float(line))

    return temperatures


def compute_average(values):
    """
    Compute the average of a list of numbers.
    """
    # TODO: Replace this with a correct average calculation.
    average = 0.0
    for value in values:
        average += value
    average /= len(values)
    return average


def compute_minimum(values):
    """
    Compute the minimum value in a list of numbers.
    """
    # TODO: Replace this with a correct minimum calculation.
    minimum = values[0]
    for value in values:
        if value < minimum:
            minimum = value
    return minimum


def compute_maximum(values):
    """
    Compute the maximum value in a list of numbers.
    """
    # TODO: Replace this with a correct maximum calculation.
    maximum = values[0]
    for value in values:
        if value > maximum:
            maximum = value
    return maximum


def print_summary(values):
    """
    Print a formatted summary of the temperature data.
    """
    count = len(values)
    minimum = compute_minimum(values)
    maximum = compute_maximum(values)
    average = compute_average(values)

    # TODO: Improve this output formatting.
    print("Temperature Summary")
    print("Number of readings:", count)
    print("Minimum temperature:", minimum)
    print("Maximum temperature:", maximum)
    print("Average temperature:", average)

def plot_histogram(values):
    """
    Plot a histogram of the temperature data.
    """
    fig, ax = plt.subplots()
    ax.hist(values, bins=10, edgecolor='black')
    ax.set_title("Temperature Distribution")
    ax.set_xlabel("Temperature (F)")
    ax.set_ylabel("Frequency")
    plt.show()


def main():
    """
    Main program function.
    """
    data_file = Path(__file__).resolve().parent.parent / "data" / "temperatures.txt"
    temperatures = read_temperatures(data_file)
    print_summary(temperatures)
    plot_histogram(temperatures)


if __name__ == "__main__":
    main()
