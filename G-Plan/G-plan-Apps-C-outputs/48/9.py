
def solve_puzzle(puzzle):
    words = puzzle.split('+')
    words[-1], words[1] = words[1].split('=')
    letters = set(''.join(words))
    if len(letters) > 10:
        return "impossible"
    
    def is_valid_assignment(mapping):
        if any(mapping[word[0]] == '0' for word in words):
            return False
        return sum(int(''.join(mapping[c] for c in word)) for word in words[:-1]) == int(''.join(mapping[c] for c in words[-1]))
    
    def backtrack(mapping, idx):
        if idx == len(letters):
            if is_valid_assignment(mapping):
                return ''.join(mapping[c] for c in words[0]) + '+' + ''.join(mapping[c] for c in words[1]) + '=' + ''.join(mapping[c] for c in words[2])
            return None
        
        for digit in '0123456789':
            if digit not in mapping.values():
                mapping[letters[idx]] = digit
                result = backtrack(mapping, idx + 1)
                if result:
                    return result
                del mapping[letters[idx]]
        
        return None
    
    mapping = {}
    return backtrack(mapping, 0) or "impossible"

if __name__ == '__main__':
    puzzle = input().strip()
    print(solve_puzzle(puzzle))
