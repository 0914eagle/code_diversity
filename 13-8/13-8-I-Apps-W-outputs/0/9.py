
def get_synchronized_stones(c_stones, t_stones):
    # Initialize the synchronized stones as a copy of the input stones
    sync_stones = c_stones.copy()
    
    # Iterate through the stones and synchronize them with their neighbors
    for i in range(1, len(c_stones) - 1):
        sync_stones[i] = sync_stones[i + 1] + sync_stones[i - 1] - c_stones[i]
    
    # Return the synchronized stones
    return sync_stones

def is_synchronized(c_stones, t_stones):
    # Get the synchronized stones
    sync_stones = get_synchronized_stones(c_stones, t_stones)
    
    # Check if the synchronized stones are equal to the target stones
    if sync_stones == t_stones:
        return True
    else:
        return False

def main():
    # Read the input
    n = int(input())
    c_stones = list(map(int, input().split()))
    t_stones = list(map(int, input().split()))
    
    # Check if the stones can be synchronized
    if is_synchronized(c_stones, t_stones):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

