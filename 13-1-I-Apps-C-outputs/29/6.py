
def count_ways(n, numbers):
    # Initialize a dictionary to store the count of ways for each pair of students
    ways = {}

    # Iterate over each pair of students
    for i in range(n):
        for j in range(i+1, n):
            # Get the numbers held by the two students
            x = numbers[i]
            y = numbers[j]

            # Check if the two numbers have a common factor other than 1
            if has_common_factor(x, y):
                # If they do, increment the count of ways for this pair of students
                ways[(i, j)] = ways.get((i, j), 0) + 1

    # Return the total count of ways modulo 10^9+7
    return sum(ways.values()) % 1000000007

def has_common_factor(x, y):
    # Iterate over the factors of x
    for i in range(2, int(x**0.5) + 1):
        # If y is a factor of x, return True
        if x % i == 0 and y % i == 0:
            return True

    # If no common factor is found, return False
    return False

