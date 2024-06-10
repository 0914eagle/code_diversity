
def get_number_of_ways(n, k):
    # Initialize a list to store the numbers on the houses' plaques
    plaques = [0] * (n + 1)
    # Initialize a variable to store the number of ways to write the numbers on the houses' plaques
    number_of_ways = 0
    
    # Iterate over the houses
    for i in range(1, n + 1):
        # If the house is the first house, set the number on its plaque to 1
        if i == 1:
            plaques[i] = 1
        # If the house is not the first house, set the number on its plaque to the sum of the numbers on the plaques of the previous houses
        else:
            plaques[i] = sum(plaques[1:i])
    
    # Iterate over the houses
    for i in range(1, n + 1):
        # If the house is the first house, set the number of ways to write the numbers on the houses' plaques to the number of ways to write the numbers on the houses' plaques up to the current house
        if i == 1:
            number_of_ways = number_of_ways + 1
        # If the house is not the first house, set the number of ways to write the numbers on the houses' plaques to the sum of the number of ways to write the numbers on the houses' plaques up to the current house and the number of ways to write the numbers on the houses' plaques up to the previous house
        else:
            number_of_ways = (number_of_ways + plaques[i - 1]) % 1000000007
    
    # Return the number of ways to write the numbers on the houses' plaques modulo 1000000007
    return number_of_ways

def main():
    # Read the input
    n, k = map(int, input().split())
    # Call the function to get the number of ways to write the numbers on the houses' plaques
    number_of_ways = get_number_of_ways(n, k)
    # Print the result
    print(number_of_ways)

if __name__ == '__main__':
    main()

