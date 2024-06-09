
def solve_cryptarithmetic_puzzle(puzzle):
    words = puzzle.split('+')
    letters = set()
    for word in words:
        letters |= set(word)
    letters = sorted(letters)
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assignments = {}
    for letter in letters:
        assignments[letter] = None
    for letter in letters:
        for digit in digits:
            if is_valid_assignment(assignments, letter, digit):
                assignments[letter] = digit
                break
    if all(assignments.values()):
        return get_solution(puzzle, assignments)
    else:
        return 'impossible'

def is_valid_assignment(assignments, letter, digit):
    if letter == letter.upper():
        return digit != 0
    else:
        return digit not in assignments.values()

def get_solution(puzzle, assignments):
    solution = ''
    for char in puzzle:
        if char in assignments:
            solution += str(assignments[char])
        else:
            solution += char
    return solution

if __name__ == '__main__':
    puzzle = input()
    print(solve_cryptarithmetic_puzzle(puzzle))

