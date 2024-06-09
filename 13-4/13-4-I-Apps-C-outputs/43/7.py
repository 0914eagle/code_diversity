
import itertools

def solve(r, s, m, d, n, b, dishes):
    # Initialize a set to store the different dinner experiences
    dinner_experiences = set()

    # Iterate over the starter dishes
    for starter in dishes[:s]:
        # Iterate over the main dishes
        for main in dishes[s:s+m]:
            # Iterate over the desserts
            for dessert in dishes[s+m:]:
                # Check if the starter, main, and dessert are compatible
                if are_compatible(starter, main, dessert, n, b):
                    # If they are compatible, add the dinner experience to the set
                    dinner_experiences.add((starter, main, dessert))

    # Return the number of different dinner experiences
    return len(dinner_experiences)

def are_compatible(starter, main, dessert, n, b):
    # Initialize a set to store the incompatible dishes
    incompatible_dishes = set()

    # Iterate over the incompatible dish pairs
    for pair in itertools.combinations(range(1, s+m+d+1), 2):
        # Check if the current pair contains the starter, main, and dessert
        if pair[0] in (starter, main, dessert) and pair[1] in (starter, main, dessert):
            # If they do, add the dishes to the set
            incompatible_dishes.add(pair[0])
            incompatible_dishes.add(pair[1])

    # Check if the set of incompatible dishes is empty
    if len(incompatible_dishes) == 0:
        # If it is, return True
        return True
    else:
        # If it is not, return False
        return False

def main():
    # Read the input
    r, s, m, d, n = map(int, input().split())
    b = list(map(int, input().split()))
    dishes = []
    for i in range(s+m+d):
        k, *ingredients = map(int, input().split())
        dishes.append(ingredients)

    # Solve the problem
    result = solve(r, s, m, d, n, b, dishes)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()

