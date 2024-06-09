
def get_jokes(n, jokes, supervisors):
    # Initialize a set to store the jokes
    seen_jokes = set()
    
    # Iterate over the employees
    for employee in range(1, n + 1):
        # If the employee is not Petar
        if employee != 1:
            # Get the jokes told by the employee
            employee_jokes = jokes[employee - 1]
            
            # If the employee's direct supervisor is not invited
            if supervisors[employee - 1] not in seen_jokes:
                # Skip this employee
                continue
            
            # If the set of jokes the employee's supervisor tells and the employee don't form a set of consecutive numbers
            if not is_consecutive(seen_jokes, employee_jokes):
                # Skip this employee
                continue
        
        # Add the employee's jokes to the set
        seen_jokes.update(employee_jokes)
    
    # Return the number of different sets of jokes
    return len(seen_jokes)

def is_consecutive(set1, set2):
    # Sort the sets
    sorted_set1 = sorted(set1)
    sorted_set2 = sorted(set2)
    
    # Initialize a flag to indicate if the sets are consecutive
    is_consecutive = True
    
    # Iterate over the elements of the first set
    for i in range(len(sorted_set1) - 1):
        # If the difference between the adjacent elements is not 1
        if sorted_set1[i + 1] - sorted_set1[i] != 1:
            # Set the flag to False
            is_consecutive = False
            break
    
    # Iterate over the elements of the second set
    for i in range(len(sorted_set2) - 1):
        # If the difference between the adjacent elements is not 1
        if sorted_set2[i + 1] - sorted_set2[i] != 1:
            # Set the flag to False
            is_consecutive = False
            break
    
    # Return the flag
    return is_consecutive

def main():
    # Read the input
    n = int(input())
    jokes = [set(map(int, input().split())) for _ in range(n)]
    supervisors = [int(input()) for _ in range(n - 1)]
    
    # Call the function to get the number of different sets of jokes
    result = get_jokes(n, jokes, supervisors)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

