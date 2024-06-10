
def get_max_distance(n, x, a, b):
    if a == b:
        return 0
    
    # Initialize the maximum distance as the minimum distance between a and b
    max_dist = abs(a - b)
    
    # Loop through all possible positions for the second rival
    for pos in range(1, n + 1):
        # If the position is not adjacent to a, skip it
        if abs(pos - a) != 1:
            continue
        
        # Calculate the distance between the two rivals after swapping them
        dist = abs(pos - b)
        
        # If the distance is greater than the current maximum distance, update the maximum distance
        if dist > max_dist:
            max_dist = dist
    
    return max_dist

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        n, x, a, b = map(int, input().split())
        print(get_max_distance(n, x, a, b))

if __name__ == '__main__':
    main()

