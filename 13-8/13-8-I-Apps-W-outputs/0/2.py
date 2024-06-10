
def get_synchronized_stones(c_stones, t_stones):
    # Initialize a list to store the synchronized stones
    synchronized_stones = []
    
    # Loop through the charges of Grigory's stones
    for i in range(len(c_stones)):
        # Find the index of the stone with the same charge in Andrew's list
        j = t_stones.index(c_stones[i])
        
        # If the stone is not already synchronized, synchronize it with its neighboring stones
        if j != i:
            # Calculate the new charge of the stone
            new_charge = c_stones[i - 1] + c_stones[i + 1] - c_stones[i]
            
            # Add the synchronized stone to the list
            synchronized_stones.append(new_charge)
        else:
            # If the stone is already synchronized, add it to the list as is
            synchronized_stones.append(c_stones[i])
    
    return synchronized_stones

def main():
    # Read the input
    n = int(input())
    c_stones = list(map(int, input().split()))
    t_stones = list(map(int, input().split()))
    
    # Check if there exists a sequence of synchronization operations that transforms Grigory's stones into Andrew's stones
    if get_synchronized_stones(c_stones, t_stones) == t_stones:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

