
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
    # If the ID is the same length as the pattern, check if it satisfies the pattern
    if len(id) == len(pattern):
        for i in range(len(id)):
            if id[i] != '1' and pattern[i] != '*':
                return False
        return True
    
    # If the ID is shorter than the pattern, check if any substring of the ID satisfies the pattern
    for i in range(len(id)):
        if satisfies_pattern(id[i:], pattern):
            return True
    return False

def main():
    n = int(input())
    pattern = input()
    valid_ids = get_valid_ids(n, pattern)
    print(len(valid_ids))

if __name__ == '__main__':
    main()

