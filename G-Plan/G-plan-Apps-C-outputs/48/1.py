
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words = [word.split('=') for word in words]
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_solution(solution):
        for i, word in enumerate(words):
            if sum(int(solution[c]) * (10 ** (len(word) - j - 1)) for j, c in enumerate(word)) != int(words[i]):
                return False
        return True
    
    def backtrack(solution, index):
        if index == len(letters):
            if is_valid_solution(solution):
                return solution
            return None
        
        for digit in range(10):
            if digit == 0 and letters[index] in words[0][0] + words[1][0] + words[2][0]:
                continue
            if digit in solution.values():
                continue
            
            solution[letters[index]] = digit
            result = backtrack(solution, index + 1)
            if result:
                return result
            solution.pop(letters[index])
        
        return None
    
    initial_solution = {}
    return ''.join(str(backtrack(initial_solution, 0)[c]) for c in puzzle)

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
