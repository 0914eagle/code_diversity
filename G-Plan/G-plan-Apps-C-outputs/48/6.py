
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words = [word.split('=') for word in words]
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_assignment(assignment):
        return all(assignment[letter] != '0' for letter in letters) and len(set(assignment.values())) == len(letters)
    
    def solve(words, assignment, idx):
        if idx == len(words):
            if sum(int(''.join(assignment[letter] for letter in word)) for word in words[:-1]) == int(''.join(assignment[letter] for letter in words[-1])):
                return True
            return False
        
        for char in words[idx]:
            if char not in assignment:
                for digit in '1234567890':
                    assignment[char] = digit
                    if is_valid_assignment(assignment) and solve(words, assignment, idx + 1):
                        return True
                    del assignment[char]
        
        return False
    
    assignment = {}
    if solve(words, assignment, 0):
        return '+'.join(''.join(assignment[letter] for letter in word) for word in words) + '=' + ''.join(assignment[letter] for letter in words[-1])
    else:
        return "impossible"

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
