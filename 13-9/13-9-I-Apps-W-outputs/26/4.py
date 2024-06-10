
def get_minimum_flats_to_visit(n, s):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of flats to visit
    min_flats = 0
    # Iterate through the row of flats
    for i in range(n):
        # If the type of Pokemon in the current flat is not in the visited types set, add it to the set and increment the minimum number of flats to visit
        if s[i] not in visited_types:
            visited_types.add(s[i])
            min_flats += 1
    # Return the minimum number of flats to visit
    return min_flats

def main():
    n = int(input())
    s = input()
    print(get_minimum_flats_to_visit(n, s))

if __name__ == '__main__':
    main()

