
def get_maximum_distance(n, x, a, b):
    # Initialize the distance between the rivals
    distance = abs(a - b)
    
    # Loop through each swap
    for i in range(x):
        # Get the positions of the two adjacent students
        pos1 = (a + i) % n
        pos2 = (b + i) % n
        
        # Calculate the distance between the two students after the swap
        new_distance = abs(pos1 - pos2)
        
        # Update the distance if the new distance is greater
        if new_distance > distance:
            distance = new_distance
    
    # Return the maximum distance
    return distance

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the input
        n, x, a, b = map(int, input().split())
        
        # Get the maximum distance
        distance = get_maximum_distance(n, x, a, b)
        
        # Print the result
        print(distance)

if __name__ == '__main__':
    main()

