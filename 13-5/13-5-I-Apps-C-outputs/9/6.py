
import itertools

def get_valid_ids(n, pattern):
    # Generate all possible binary strings of length n
    all_ids = [''.join(id) for id in itertools.product('01', repeat=n)]
    
    # Filter out ids that do not satisfy the pattern
    valid_ids = []
    for id in all_ids:
        if satisfies_pattern(id, pattern):
            valid_ids.append(id)
    
    return valid_ids

def satisfies_pattern(id, pattern):
    # If the length of the id is not equal to the length of the pattern, return False
    if len(id) != len(pattern):
        return False
    
    # If the length of the id is equal to the length of the pattern, return True if any of the following conditions is met:
    # 1. The id contains at least half 1s and the pattern contains at least half 1s.
    # 2. The id contains at least one substring that satisfies the pattern.
    if id.count('1') >= len(id) // 2 and pattern.count('1') >= len(pattern) // 2:
        return True
    elif any(id[i:i+len(pattern)] == pattern for i in range(len(id) - len(pattern) + 1)):
        return True
    else:
        return False

def get_max_members(n, pattern):
    valid_ids = get_valid_ids(n, pattern)
    return len(valid_ids)

if __name__ == '__main__':
    n = int(input())
    pattern = input()
    print(get_max_members(n, pattern))

