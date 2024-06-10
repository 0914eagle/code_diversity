
def arkady_candies(n, k, M, D):
    # Initialize variables
    max_candies = 0
    x = 1
    
    # Iterate through possible values of x
    while x <= M:
        # Calculate the number of candies that each person will receive
        candies_per_person = x
        leftover = n % x
        num_people_receiving_leftover = leftover // D
        candies_per_person += num_people_receiving_leftover
        
        # Calculate the total number of candies that Arkady will receive
        total_candies = k * candies_per_person
        
        # Update the maximum number of candies if necessary
        if total_candies > max_candies:
            max_candies = total_candies
        
        # Increase x by 1 for the next iteration
        x += 1
    
    # Return the maximum number of candies that Arkady can receive
    return max_candies

def main():
    n, k, M, D = map(int, input().split())
    print(arkady_candies(n, k, M, D))

if __name__ == '__main__':
    main()

