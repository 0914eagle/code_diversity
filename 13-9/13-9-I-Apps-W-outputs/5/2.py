
def get_lamp_states(n, k):
    # Initialize a list to store the lamp states
    lamp_states = []
    
    # Iterate over the number of lamps
    for i in range(n):
        # Read the period of time when the lamp is turned on
        l, r = map(int, input().split())
        
        # Iterate over the period of time
        for j in range(l, r + 1):
            # Add the lamp state to the list
            lamp_states.append(i)
    
    # Return the lamp states
    return lamp_states

def get_open_door_combinations(lamp_states, k):
    # Initialize a set to store the open door combinations
    open_door_combinations = set()
    
    # Iterate over the lamp states
    for i in range(len(lamp_states) - k + 1):
        # Get the combination of lamps that are turned on at the same time
        combination = tuple(lamp_states[i:i+k])
        
        # Add the combination to the set
        open_door_combinations.add(combination)
    
    # Return the open door combinations
    return open_door_combinations

def main():
    # Read the number of lamps and the number of lamps that must be turned on simultaneously
    n, k = map(int, input().split())
    
    # Get the lamp states
    lamp_states = get_lamp_states(n, k)
    
    # Get the open door combinations
    open_door_combinations = get_open_door_combinations(lamp_states, k)
    
    # Print the number of open door combinations modulo 998244353
    print(len(open_door_combinations) % 998244353)

if __name__ == '__main__':
    main()

