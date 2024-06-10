e_puzzle(puzzle):
    words = puzzle.split('+') + puzzle.split('=')  # Extracting words from the puzzle
    unique_letters = set(''.join(words))  # Finding unique letters in the puzzle
    if len(unique_letters) > 10:  # Check if more than 10 unique letters
        return "impossible"

    def is_valid_assignment(assignment):
        return all(assignment[letter] != '0' for letter in words) and len(set(assignment.values())) == len(assignment)

    def backtrack(index, assignment):
        if index == len(unique_letters):
            if is_valid_assignment(assignment):
                return assignment
            return None

        for digit in range(10):
            if str(digit) not in assignment.values():
                assignment[unique_letters[index]] = str(digit)
                result = backtrack(index + 1, assignment)
                if result:
                    return result
                assignment[unique_letters[index]] = ''  # Backtrack

        return None

    initial_assignment = {letter: '' for letter in unique_letters}
    solution = backtrack(0, initial_assignment)
    if solution:
        for letter, digit in solution.items():
            puzzle = puzzle.replace(letter, digit)
        return puzzle
    else:
        return "impossible"

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
