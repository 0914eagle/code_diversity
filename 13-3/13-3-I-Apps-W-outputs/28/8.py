
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    curr_frogs = 0
    curr_dist = 0
    stones = []
    
    # Iterate through the input array
    for i in range(len(a)):
        # If the current distance is not at the bank, add the current number of stones to the list of stones
        if curr_dist != 0:
            stones.extend([curr_dist] * a[i])
        
        # If the current distance is at the bank and there are stones, remove the first stone and add a frog
        if curr_dist == 0 and stones:
            stones.pop(0)
            curr_frogs += 1
        
        # If the current distance is at the bank and there are no stones, remove a frog
        elif curr_dist == 0 and not stones:
            curr_frogs -= 1
        
        # Update the current distance and number of frogs
        curr_dist += 1
        max_frogs = max(max_frogs, curr_frogs)
    
    # Return the maximum number of frogs that can cross the river
    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w, l = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

