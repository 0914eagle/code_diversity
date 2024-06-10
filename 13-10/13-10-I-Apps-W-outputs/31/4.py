
def get_bonds(a, b, c):
    # Find all possible combinations of bonds between the atoms
    combinations = [(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 1, 2), (1, 2, 3), (2, 0, 2), (2, 1, 3), (2, 2, 4)]
    
    # Filter out combinations that don't match the valence numbers
    valid_combinations = []
    for combination in combinations:
        if combination[0] + combination[1] + combination[2] == a and combination[1] + combination[2] + combination[0] == b and combination[2] + combination[0] + combination[1] == c:
            valid_combinations.append(combination)
    
    # If there is at least one valid combination, return any of them
    if valid_combinations:
        return valid_combinations[0]
    else:
        return "Impossible"

def main():
    a, b, c = map(int, input().split())
    print(get_bonds(a, b, c))

if __name__ == '__main__':
    main()

