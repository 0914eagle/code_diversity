
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words = [word.split('=') for word in words]
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_assignment(assignment):
        return all(assignment[letter] != '0' for word in words for letter in word[0] if letter in assignment)
    
    def backtrack(assignment, idx):
        if idx == len(letters):
            if is_valid_assignment(assignment):
                return assignment
            return None
        
        for digit in range(10):
            if str(digit) not in assignment.values():
                assignment[letters[idx]] = str(digit)
                result = backtrack(assignment, idx + 1)
                if result:
                    return result
                assignment.pop(letters[idx])
        
        return None
    
    assignment = {}
    result = backtrack(assignment, 0)
    
    if result:
        solution = puzzle
        for letter, digit in result.items():
            solution = solution.replace(letter, digit)
        return solution
    else:
        return "impossible"

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
