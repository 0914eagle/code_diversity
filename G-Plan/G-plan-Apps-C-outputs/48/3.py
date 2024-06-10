
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words = [word.split('=') for word in words]
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_assignment(assignment):
        return all(assignment[letter] != '0' for letter in letters)
    
    def solve(words, assignment, idx):
        if idx == len(letters):
            if sum(int(''.join(assignment[letter] for letter in word)) for word in words[:-1]) == int(''.join(assignment[letter] for letter in words[-1])):
                return True
            return False
        
        for digit in '0123456789':
            if digit in assignment.values():
                continue
            assignment[letters[idx]] = digit
            if is_valid_assignment(assignment) and solve(words, assignment, idx + 1):
                return True
            assignment[letters[idx]] = ''
        
        return False
    
    assignment = {letter: '' for letter in letters}
    if solve(words, assignment, 0):
        result = ''.join(assignment[letter] for letter in puzzle)
        return result
    else:
        return "impossible"

if __name__ == '__main__':
    puzzle = input().strip()
    result = solve_puzzle(puzzle)
    print(result)
