
def get_total_number_of_chairs(n, left_requirements, right_requirements):
    # Initialize a list to store the number of chairs for each circle
    num_chairs_list = []
    
    # Iterate through the input requirements and calculate the minimum number of chairs required for each circle
    for i in range(n):
        # Calculate the minimum number of chairs required for the current circle
        num_chairs = left_requirements[i] + right_requirements[i] + 1
        
        # Add the number of chairs required for the current circle to the list
        num_chairs_list.append(num_chairs)
    
    # Return the sum of the minimum number of chairs required for all circles
    return sum(num_chairs_list)

def main():
    # Read the input
    n = int(input())
    left_requirements = [int(x) for x in input().split()]
    right_requirements = [int(x) for x in input().split()]
    
    # Calculate the total number of chairs required
    total_num_chairs = get_total_number_of_chairs(n, left_requirements, right_requirements)
    
    # Print the result
    print(total_num_chairs)

if __name__ == '__main__':
    main()

