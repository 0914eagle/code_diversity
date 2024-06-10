
def get_minimum_time(sticks):
    # Sort the sticks in non-decreasing order
    sticks.sort()
    # Initialize the minimum time to 0
    time = 0
    # Loop through the sticks and increase their length by 1 centimeter each
    for i in range(len(sticks)):
        sticks[i] += 1
        time += 1
    # Return the minimum time needed to form a triangle
    return time

def main():
    # Take input from the user
    a, b, c = map(int, input().split())
    # Create a list of sticks with the lengths entered by the user
    sticks = [a, b, c]
    # Call the get_minimum_time function and print the result
    print(get_minimum_time(sticks))

if __name__ == '__main__':
    main()

