
def get_maximum_chaos(passengers_per_coach, coach_order):
    # Calculate the total number of passengers in the train
    total_passengers = sum(passengers_per_coach)
    
    # Initialize the maximum chaos to 0
    maximum_chaos = 0
    
    # Iterate through the coaches in the order specified by the permutation
    for i in coach_order:
        # Calculate the number of passengers in the current coach
        current_coach_passengers = passengers_per_coach[i - 1]
        
        # Calculate the chaos caused by blowing up the current coach
        current_coach_chaos = current_coach_passengers - current_coach_passengers % 10
        
        # Update the maximum chaos if the current coach chaos is higher than the previous maximum chaos
        maximum_chaos = max(maximum_chaos, current_coach_chaos)
    
    # Return the maximum chaos caused by blowing up the coaches
    return maximum_chaos

def get_maximum_chaos_multiple_segments(passengers_per_coach, coach_order):
    # Calculate the total number of passengers in the train
    total_passengers = sum(passengers_per_coach)
    
    # Initialize the maximum chaos to 0
    maximum_chaos = 0
    
    # Iterate through the coaches in the order specified by the permutation
    for i in coach_order:
        # Calculate the number of passengers in the current coach
        current_coach_passengers = passengers_per_coach[i - 1]
        
        # Calculate the chaos caused by blowing up the current coach
        current_coach_chaos = current_coach_passengers - current_coach_passengers % 10
        
        # Update the maximum chaos if the current coach chaos is higher than the previous maximum chaos
        maximum_chaos = max(maximum_chaos, current_coach_chaos)
    
    # Calculate the total chaos caused by blowing up all the coaches
    total_chaos = maximum_chaos * len(coach_order)
    
    # Return the total chaos
    return total_chaos

if __name__ == '__main__':
    # Read the input
    n = int(input())
    passengers_per_coach = list(map(int, input().split()))
    coach_order = list(map(int, input().split()))
    
    # Calculate the maximum chaos caused by blowing up the coaches
    maximum_chaos = get_maximum_chaos(passengers_per_coach, coach_order)
    
    # Calculate the total chaos caused by blowing up all the coaches
    total_chaos = get_maximum_chaos_multiple_segments(passengers_per_coach, coach_order)
    
    # Print the maximum chaos
    print(maximum_chaos)
    
    # Print the total chaos
    print(total_chaos)

