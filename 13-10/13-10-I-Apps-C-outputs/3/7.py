
def get_maximum_chaos(coaches, passengers, coach_order):
    # Initialize a list to store the chaos for each coach
    coach_chaos = [0] * len(coaches)
    
    # Iterate through the coaches in the order specified by the permutation
    for i in range(len(coaches)):
        # Get the current coach number and the number of passengers
        coach_num = coach_order[i]
        num_passengers = passengers[coach_num - 1]
        
        # Calculate the chaos for the current coach
        coach_chaos[coach_num - 1] = int(num_passengers / 10) * 10
    
    # Return the maximum chaos among all the coaches
    return max(coach_chaos)

def main():
    # Read the input data
    num_coaches = int(input())
    passengers = [int(x) for x in input().split()]
    coach_order = [int(x) for x in input().split()]
    
    # Calculate the maximum chaos
    max_chaos = get_maximum_chaos(num_coaches, passengers, coach_order)
    
    # Print the result
    print(max_chaos)

if __name__ == '__main__':
    main()

