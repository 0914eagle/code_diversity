
def get_min_time(a, b, c):
    # Sort the sticks by length in non-decreasing order
    sticks = sorted([a, b, c])
    
    # Initialize the minimum time to 0
    min_time = 0
    
    # Loop through the sticks and increase their length by one centimeter each
    for i in range(len(sticks)):
        min_time += 1
        sticks[i] += 1
        
        # If the sum of the lengths of the sticks is greater than the largest stick, return the current minimum time
        if sum(sticks) > max(sticks):
            return min_time
    
    # If the sum of the lengths of the sticks is not greater than the largest stick, return -1
    return -1

def main():
    a, b, c = map(int, input().split())
    print(get_min_time(a, b, c))

if __name__ == '__main__':
    main()

