
def get_min_visits(n, flat_types):
    # Initialize a set to store the types of Pokemons visited
    visited_types = set()
    # Initialize a variable to store the minimum number of visits
    min_visits = 0
    # Loop through each flat and its type
    for i, flat_type in enumerate(flat_types):
        # If the type of Pokemon in the current flat is not visited yet, visit it and add it to the set of visited types
        if flat_type not in visited_types:
            visited_types.add(flat_type)
            min_visits += 1
        # If all types of Pokemons are visited, break the loop
        if len(visited_types) == n:
            break
    return min_visits

def main():
    n = int(input())
    flat_types = input()
    print(get_min_visits(n, flat_types))

if __name__ == '__main__':
    main()

