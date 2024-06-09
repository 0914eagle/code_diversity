
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    curr_frogs = 0
    prev_frog = 0
    next_frog = 0
    
    # Iterate through the array of stones
    for i in range(len(a)):
        # If there are no stones at the current distance, skip to the next iteration
        if a[i] == 0:
            continue
        
        # If the current distance is within the jump length of the frogs, add the number of frogs that can cross
        if i <= l:
            curr_frogs += a[i]
        
        # If the current distance is greater than the jump length of the frogs, add the number of frogs that can cross and subtract the number of frogs that will drown
        else:
            curr_frogs += a[i] - 1
        
        # Update the maximum number of frogs if necessary
        if curr_frogs > max_frogs:
            max_frogs = curr_frogs
        
        # Update the previous frog position
        prev_frog = i
    
    # If the last frog can cross the river, add it to the total number of frogs
    if w - prev_frog <= l:
        max_frogs += 1
    
    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w = int(input())
    l = int(input())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

