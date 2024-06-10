
def get_maximum_candies(n, k, M, D):
    # Initialize a list to store the maximum number of candies that can be given to each person
    max_candies = [0] * k
    
    # Iterate through the possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies that each person will receive
        candies_per_person = x
        leftover = n % x
        if leftover > 0:
            candies_per_person += 1
        
        # Check if the number of candies given to each person is less than or equal to D
        if candies_per_person <= D:
            # Update the maximum number of candies that can be given to each person
            for i in range(k):
                max_candies[i] = max(max_candies[i], candies_per_person)
    
    # Return the maximum number of candies that Arkady can receive
    return sum(max_candies)

def main():
    n, k, M, D = map(int, input().split())
    print(get_maximum_candies(n, k, M, D))

if __name__ == '__main__':
    main()

