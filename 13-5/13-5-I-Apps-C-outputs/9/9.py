
import itertools

def get_valid_ids(n, pattern):
    # Generate all possible binary strings of length n
    all_ids = [''.join(id) for id in itertools.product('01', repeat=n)]
    
    # Filter out IDs that do not satisfy the pattern
    valid_ids = []
    for id in all_ids:
        if satisfies_pattern(id, pattern):
            valid_ids.append(id)
    
    return valid_ids

def satisfies_pattern(id, pattern):
    # Check if the ID satisfies the pattern
    if len(id) != len(pattern):
        return False
    
    for i in range(len(id)):
        if id[i] != '1' and pattern[i] != '*':
            return False
    
    return True

def get_max_members(n, pattern):
    # Get all valid IDs
    valid_ids = get_valid_ids(n, pattern)
    
    # Return the maximum number of members
    return 2 ** n - len(valid_ids)

if __name__ == '__main__':
    n = int(input())
    pattern = input()
    print(get_max_members(n, pattern))

