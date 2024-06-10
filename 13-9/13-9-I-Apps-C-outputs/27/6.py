
def get_total_chairs(n, left_requirements, right_requirements):
    # Initialize a list to store the number of chairs for each circle
    chairs_per_circle = []
    
    # Iterate through the input lists
    for i in range(n):
        # Calculate the total number of chairs required for the current circle
        total_chairs = left_requirements[i] + right_requirements[i] + 1
        
        # Add the total number of chairs to the list
        chairs_per_circle.append(total_chairs)
    
    # Return the sum of all chairs required
    return sum(chairs_per_circle)

def main():
    # Read the number of guests
    n = int(input())
    
    # Read the left and right requirements for each guest
    left_requirements = []
    right_requirements = []
    for i in range(n):
        left, right = map(int, input().split())
        left_requirements.append(left)
        right_requirements.append(right)
    
    # Call the get_total_chairs function and print the result
    total_chairs = get_total_chairs(n, left_requirements, right_requirements)
    print(total_chairs)

if __name__ == '__main__':
    main()

