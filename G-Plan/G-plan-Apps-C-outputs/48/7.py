
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words = [word.split('=') for word in words]
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_assignment(assignment):
        if '0' in assignment.values():
            return False
        return len(set(assignment.values())) == len(letters)
    
    def solve(words, assignment, idx):
        if idx == len(letters):
            if sum(int(''.join([assignment[c] for c in word])) for word in words[:-1]) == int(''.join([assignment[c] for c in words[-1]])):
                return True
            return False
        
        for digit in range(10):
            if str(digit) not in assignment.values():
                assignment[letters[idx]] = str(digit)
                if is_valid_assignment(assignment) and solve(words, assignment, idx + 1):
                    return True
                assignment[letters[idx]] = ''
        
        return False
    
    assignment = {letter: '' for letter in letters}
    if solve(words, assignment, 0):
        result = '+'.join([word.replace('=', '') for word in words]) + '=' + words[-1]
        return result.replace(''.join(assignment.values()), ''.join(assignment[c] for c in words[-1]))
    else:
        return "impossible"

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
