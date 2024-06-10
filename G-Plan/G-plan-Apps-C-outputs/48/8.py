
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words = [word.split('=') for word in words]
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_assignment(assignment):
        if any(assignment[letter] == '0' for letter in letters):
            return False
        return sum(int(''.join(assignment[letter] for letter in word)) for word in words[:-1]) == int(''.join(assignment[letter] for letter in words[-1]))
    
    def backtrack(assignment, idx):
        if idx == len(letters):
            if is_valid_assignment(assignment):
                return ''.join(assignment[letter] for letter in words[0]) + '+' + ''.join(assignment[letter] for letter in words[1]) + '=' + ''.join(assignment[letter] for letter in words[2])
            return None
        
        for digit in range(10):
            if str(digit) not in assignment.values():
                assignment[letters[idx]] = str(digit)
                result = backtrack(assignment, idx + 1)
                if result:
                    return result
                assignment[letters[idx]] = ''
        
        return None
    
    assignment = {letter: '' for letter in letters}
    return backtrack(assignment, 0)

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
