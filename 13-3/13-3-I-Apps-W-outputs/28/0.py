
def f1(w, l, a):
    # Initialize variables
    max_frogs = 0
    current_frogs = 0
    current_distance = 0
    stones = []
    
    # Iterate through the input array
    for i in range(len(a)):
        # If there are stones at the current distance, add them to the list of available stones
        if a[i] > 0:
            for j in range(a[i]):
                stones.append(i)
        
        # If there are enough stones to cross the river, update the maximum number of frogs that can cross
        if len(stones) >= current_frogs + 1:
            max_frogs = max(max_frogs, current_frogs + 1)
            current_frogs += 1
            current_distance += l
        
        # If there are no more stones at the current distance, move to the next distance
        else:
            current_distance += l
            current_frogs = 0
    
    return max_frogs

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    w, l = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(w, l, a))

