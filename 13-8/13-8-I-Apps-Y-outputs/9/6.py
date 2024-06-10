
def get_maximum_candies(n, k):
    
    # Initialize variables
    min_candies = 0
    max_candies = n
    while min_candies <= max_candies:
        # Calculate the middle value
        mid_candies = (min_candies + max_candies) // 2
        # Check if Santa is satisfied
        if is_santa_satisfied(n, k, mid_candies):
            # Update the minimum number of candies
            min_candies = mid_candies + 1
        else:
            # Update the maximum number of candies
            max_candies = mid_candies - 1
    
    # Return the maximum number of candies Santa can give
    return min_candies

def is_santa_satisfied(n, k, mid_candies):
    
    # Initialize variables
    count = 0
    i = 1
    while i <= k:
        # Calculate the number of candies for the current kid
        num_candies = mid_candies * i
        # Check if the current kid has at least mid_candies + 1 candies
        if num_candies >= mid_candies + 1:
            # Increment the count
            count += 1
        # Check if the current kid has more than mid_candies + 1 candies
        if num_candies > mid_candies + 1:
            # Break the loop
            break
        # Increment the loop variable
        i += 1
    
    # Check if the number of kids with at least mid_candies + 1 candies is less than or equal to the half of the total number of kids
    if count <= k // 2:
        # Santa is satisfied
        return True
    else:
        # Santa is not satisfied
        return False

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through the test cases
    for i in range(t):
        # Read the number of candies and the number of kids
        n, k = map(int, input().split())
        
        # Call the get_maximum_candies function
        result = get_maximum_candies(n, k)
        
        # Print the result
        print(result)

if __name__ == '__main__':
    main()

