
def get_max_value(values):
    # Initialize the maximum value to the first value
    max_value = values[0]
    # Iterate through the remaining values
    for i in range(1, len(values)):
        # Calculate the average of the current value and the maximum value
        avg = (values[i] + max_value) / 2
        # Update the maximum value if the average is greater than the current maximum value
        if avg > max_value:
            max_value = avg
    return max_value

def main():
    # Read the number of ingredients and their values from stdin
    n = int(input())
    values = list(map(int, input().split()))
    # Calculate the maximum value of the last ingredient
    max_value = get_max_value(values)
    # Print the maximum value
    print(max_value)

if __name__ == '__main__':
    main()

