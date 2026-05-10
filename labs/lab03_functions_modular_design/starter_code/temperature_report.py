def read_temperatures(filename):
    # open the file called ~/data/june_temperatures.txt for reading
    # read each line of the file, stripping whitespace and converting to an integer
    # return a list of the temperatures
    f = open(filename, "r")
    temperatures = []
    for line in f:
        line = line.strip()
        if line != "":
            temperatures.append(int(line))
    f.close()
    return temperatures

def calculate_average(values):
    total = 0
    average = 0
    for value in values:
        total = total + value
    if len(values)!=0:
        average = total / len(values)
    return average

def find_maximum(values):
    maximum = values[0]
    for value in values:
        if value > maximum:
            maximum = value
    return maximum

def find_minimum(values):
    minimum = values[0]
    for value in values:
        if value < minimum:
            minimum = value
    return minimum

def count_above_threshold(values, threshold):
    count = 0
    for value in values:
        if value > threshold:
            count = count + 1
    return count

def print_report(values):
    # calculate the average, maximum, minimum, and count of temperatures above 80
    average = calculate_average(values)
    maximum = find_maximum(values)
    minimum = find_minimum(values)
    count = count_above_threshold(values, 80)

    # print the report
    print("Temperature Report")
    print("------------------")
    print("Average temperature:", average)
    print("Maximum temperature:", maximum)
    print("Minimum temperature:", minimum)
    print("Temperatures above 80:", count)

def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

if __name__ == "__main__":
    main()
