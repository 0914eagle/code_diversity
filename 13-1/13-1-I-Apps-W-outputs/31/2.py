
def is_same_configuration(puzzle1, puzzle2):
    return puzzle1 == puzzle2

def solve_puzzle(puzzle):
    if puzzle[0] == 'A' and puzzle[1] == 'B':
        return 'AB'
    elif puzzle[0] == 'A' and puzzle[1] == 'C':
        return 'AC'
    elif puzzle[0] == 'B' and puzzle[1] == 'A':
        return 'BA'
    elif puzzle[0] == 'B' and puzzle[1] == 'C':
        return 'BC'
    elif puzzle[0] == 'C' and puzzle[1] == 'A':
        return 'CA'
    elif puzzle[0] == 'C' and puzzle[1] == 'B':
        return 'CB'
    else:
        return puzzle

def main():
    puzzle1 = input()
    puzzle2 = input()
    if is_same_configuration(puzzle1, puzzle2):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

