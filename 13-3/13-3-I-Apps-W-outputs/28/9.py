
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    curr_frogs = 0
    curr_pos = 0
    stones = []
    
    # Add stones to the list
    for i in range(len(a)):
        if a[i] > 0:
            stones.append(i)
    
    # Iterate through the stones
    for stone in stones:
        # Check if the stone is within jumping distance
        if stone - curr_pos <= l:
            curr_frogs += 1
            curr_pos = stone
        else:
            max_frogs = max(max_frogs, curr_frogs)
            curr_frogs = 0
            curr_pos = stone
    
    # Add the last frog
    max_frogs = max(max_frogs, curr_frogs + 1)
    
    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

