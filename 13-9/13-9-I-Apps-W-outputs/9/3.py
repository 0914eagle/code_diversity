
def get_max_distance(n, x, a, b):
    if x == 0:
        return abs(a - b)
    
    # Initialize the maximum distance as the current distance between the rivals
    max_distance = abs(a - b)
    
    # Loop through each possible swap
    for i in range(1, n):
        # Calculate the distance between the rivals after the swap
        distance = abs(a - b - 2 * i)
        
        # If the distance is greater than the current maximum distance, update the maximum distance
        if distance > max_distance:
            max_distance = distance
    
    return max_distance

def main():
    t = int(input())
    
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_max_distance(n, x, a, b))

if __name__ == '__main__':
    main()

