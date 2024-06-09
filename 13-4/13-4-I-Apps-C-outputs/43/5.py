
import itertools

def solve(r, s, m, d, n, b, incompatible_dishes):
    # Initialize a set to store all possible dinner experiences
    dinner_experiences = set()

    # Iterate over all possible combinations of dishes and brands
    for dishes in itertools.product(range(1, s+m+d+1), repeat=r):
        # Check if the current combination of dishes is incompatible
        if any(dishes[i-1] in incompatible_dishes[j-1] for i in dishes for j in dishes):
            continue

        # Add the current combination of dishes to the set of dinner experiences
        dinner_experiences.add(frozenset(dishes))

    # Return the number of dinner experiences
    return len(dinner_experiences)

# Main function
if __name__ == "__main__":
    # Read input from stdin
    r, s, m, d, n = map(int, input().split())
    b = list(map(int, input().split()))
    incompatible_dishes = [set(map(int, input().split())) for _ in range(n)]

    # Call the solve function and print the result
    result = solve(r, s, m, d, n, b, incompatible_dishes)
    if result <= 10**18:
        print(result)
    else:
        print("too many")

