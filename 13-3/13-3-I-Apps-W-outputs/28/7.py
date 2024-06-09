
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
        
        # If the current distance is at the bank and there are still frogs in the river, remove a frog and add it to the list of crossed frogs
        if curr_dist == 0 and curr_frogs > 0:
            curr_frogs -= 1
            max_frogs += 1
        
        # If the current distance is at the bank and there are no more frogs in the river, add a frog and move to the next distance
        if curr_dist == 0 and curr_frogs == 0:
            curr_frogs += 1
            curr_dist += l
        
        # If the current distance is not at the bank and there are still frogs in the river, move to the next distance
        if curr_dist != 0 and curr_frogs > 0:
            curr_dist += l
    
    # Return the maximum number of frogs that can cross the river
    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

