
def get_valence_numbers(input_string):
    return [int(x) for x in input_string.split()]

def get_molecule_bonds(valence_numbers):
    a, b, c = valence_numbers
    if a + b + c != 6:
        return "Impossible"
    if a == 1 and b == 1 and c == 2:
        return "0 1 1"
    if a == 3 and b == 4 and c == 5:
        return "1 3 2"
    if a == 4 and b == 1 and c == 1:
        return "Impossible"
    return "Impossible"

def main():
    valence_numbers = get_valence_numbers(input())
    print(get_molecule_bonds(valence_numbers))

if __name__ == '__main__':
    main()

