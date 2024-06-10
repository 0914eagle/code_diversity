
def get_min_max_x(n, d, b, a):
    # Initialize variables
    x_1 = 0
    x_2 = 0
    rooms_visited = set()
    
    # Iterate through each room
    for i in range(1, n+1):
        # Check if the room has been visited
        if i not in rooms_visited:
            # Get the number of students in the room
            num_students = a[i-1]
            
            # Check if the number of students is different from the official number
            if num_students != b:
                # Increment the number of rooms with different numbers
                x_1 += 1
                x_2 += 1
                
                # Add the room to the set of visited rooms
                rooms_visited.add(i)
            
            # Check if the room is evenly divisible by d
            if i % d == 0:
                # Increment the number of rooms with different numbers
                x_1 += 1
                x_2 += 1
                
                # Add the room to the set of visited rooms
                rooms_visited.add(i)
    
    # Return the minimum of x_1 and x_2
    return min(x_1, x_2)

def main():
    # Read the input
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the function to get the minimum of x_1 and x_2
    min_x = get_min_max_x(n, d, b, a)
    
    # Print the output
    print(min_x)

if __name__ == '__main__':
    main()

