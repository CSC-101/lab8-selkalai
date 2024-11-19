import sys
#Task 2:

#Write a program that takes a single command-line argument.
# This argument should be the name of a file to open for reading (if the argument is
# not provided or the file cannot be opened, then print an error message and terminate
# the program using exit). - because of this I will use error handling:

#Your program should open the file and read each line until the entire contents
# have been read. Each line in the file is expected to consist of two float values
# (how can you split a line into these two separate values? - using .strip and .split).
# For each line, convert the float values and print their sum.
# If a line is missing a value or if one of the values cannot be converted,
# then print an error message for that line, but continue processing the remaining
# lines.

def main():
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            line_num = 1
            for line in file:
                line = line.strip()
                numbers = line.split()
                if len(numbers) != 2:
                    print("Error: line does not have 2 values")
                else:
                    try:
                        num_1 = float(numbers[0])
                        num_2 = float(numbers[1])
                        print(f"Sum: {num_1 + num_2}")
                    except ValueError as e:
                        print("An error occurred", e)
                line_num += 1
    except FileNotFoundError as x:
        print("An error occurred", x)

main()


