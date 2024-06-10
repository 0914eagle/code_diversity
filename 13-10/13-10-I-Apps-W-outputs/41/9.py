
def read_input():
    n = int(input())
    hamsters = input()
    return n, hamsters

def get_min_time(n, hamsters):
    # Initialize variables
    time = 0
    standing = 0
    sitting = 0

    # Loop through the hamsters and check if they are standing or sitting
    for i in range(n):
        if hamsters[i] == 'X':
            standing += 1
        else:
            sitting += 1

    # Calculate the minimum time needed to get the desired standing/sitting ratio
    if standing > sitting:
        time += (standing - sitting) // 2
    else:
        time += (sitting - standing) // 2

    return time

def get_new_hamsters(n, hamsters, time):
    # Initialize variables
    new_hamsters = ''
    standing = 0
    sitting = 0

    # Loop through the hamsters and flip them over every minute
    for i in range(n):
        if hamsters[i] == 'X':
            if standing < time:
                new_hamsters += 'x'
                sitting += 1
            else:
                new_hamsters += 'X'
                standing += 1
        else:
            if sitting < time:
                new_hamsters += 'X'
                standing += 1
            else:
                new_hamsters += 'x'
                sitting += 1

    return new_hamsters

def main():
    # Read the input
    n, hamsters = read_input()

    # Get the minimum time needed to get the desired standing/sitting ratio
    time = get_min_time(n, hamsters)

    # Get the new hamsters' position after Pasha makes the required changes
    new_hamsters = get_new_hamsters(n, hamsters, time)

    # Print the output
    print(time)
    print(new_hamsters)

if __name__ == '__main__':
    main()

