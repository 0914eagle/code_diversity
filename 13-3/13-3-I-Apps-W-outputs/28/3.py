
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    curr_frogs = 0
    curr_pos = 0
    stones = []
    
    # Add stones to the list
    for i in range(w-1):
        if a[i] > 0:
            stones.append(i+1)
    
    # Sort the stones by their distance from the current position
    stones.sort()
    
    # Iterate through the stones and calculate the maximum number of frogs that can cross the river
    for stone in stones:
        if stone - curr_pos <= l:
            curr_frogs += 1
            curr_pos = stone
        else:
            max_frogs = max(max_frogs, curr_frogs)
            curr_frogs = 1
            curr_pos = stone
    
    # Return the maximum number of frogs that can cross the river
    return max(max_frogs, curr_frogs)

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

