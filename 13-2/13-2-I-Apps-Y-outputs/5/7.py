
def get_earliest_time_to_reach_x(x):
    # Initialize the earliest time to reach x as 0
    earliest_time = 0

    # Loop until the kangaroo reaches x
    while x > 0:
        # Check if the kangaroo can reach x by jumping to the right
        if x % earliest_time == 0:
            # If so, update the earliest time and break the loop
            earliest_time = x // earliest_time
            break
        # Otherwise, increment the earliest time by 1
        earliest_time += 1

    # Return the earliest time to reach x
    return earliest_time

if __name__ == '__main__':
    x = int(input())
    print(get_earliest_time_to_reach_x(x))

