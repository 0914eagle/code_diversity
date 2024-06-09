
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    curr_frogs = 0
    curr_pos = 0
    stones = []
    
    # Iterate through the input array
    for i in range(len(a)):
        # If there are stones at the current position, add them to the list of available stones
        if a[i] > 0:
            stones.extend([i+1] * a[i])
    
    # Sort the list of available stones in ascending order
    stones.sort()
    
    # Iterate through the list of available stones
    for stone in stones:
        # If the current position plus the length of the frog's jump is less than or equal to the stone, the frog can jump to the stone
        if curr_pos + l <= stone:
            curr_frogs += 1
            curr_pos = stone
        # If the current position plus the length of the frog's jump is greater than the stone, the frog cannot jump to the stone and must cross the river on its own
        else:
            max_frogs = max(max_frogs, curr_frogs)
            curr_frogs = 0
            curr_pos = 0
    
    # Return the maximum number of frogs that can cross the river
    return max(max_frogs, curr_frogs)

def f2(...):
    ...

if __name__ == '__main__':
    w, l = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

