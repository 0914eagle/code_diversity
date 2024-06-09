
import sys

def solve(N, M):
    # Calculate the number of possible combinations of toppings
    num_combinations = 2**N
    
    # Initialize a list to store the number of sets of bowls of ramen that satisfy the conditions
    num_sets = []
    
    # Iterate over each combination of toppings
    for i in range(num_combinations):
        # Convert the binary representation of the combination to a list of booleans
        # representing whether each topping is included or not
        toppings = [bool(i & (1 << j)) for j in range(N)]
        
        # Count the number of sets of bowls of ramen that satisfy the conditions
        num_sets.append(count_sets(toppings, M))
    
    # Return the sum of the number of sets of bowls of ramen that satisfy the conditions
    # modulo M
    return sum(num_sets) % M

def count_sets(toppings, M):
    # Initialize a list to store the number of sets of bowls of ramen that satisfy the conditions
    num_sets = [0] * len(toppings)
    
    # Iterate over each topping
    for i, topping in enumerate(toppings):
        # If the topping is included, count the number of sets of bowls of ramen that satisfy the conditions
        if topping:
            num_sets[i] = count_sets_helper(toppings, i, M)
    
    # Return the sum of the number of sets of bowls of ramen that satisfy the conditions
    # modulo M
    return sum(num_sets) % M

def count_sets_helper(toppings, i, M):
    # If the topping is the last topping, return 1
    if i == len(toppings) - 1:
        return 1
    
    # Initialize a list to store the number of sets of bowls of ramen that satisfy the conditions
    num_sets = [0] * len(toppings)
    
    # Iterate over each topping after the current topping
    for j in range(i + 1, len(toppings)):
        # If the topping is included, count the number of sets of bowls of ramen that satisfy the conditions
        if toppings[j]:
            num_sets[j] = count_sets_helper(toppings, j, M)
    
    # Return the sum of the number of sets of bowls of ramen that satisfy the conditions
    # modulo M
    return sum(num_sets) % M

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))

