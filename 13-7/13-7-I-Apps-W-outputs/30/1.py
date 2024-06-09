
import itertools

def solve(n, s):
    # convert the input sequence to a list of pairs
    pairs = [(a, b) for a, b in s]
    
    # initialize the number of good permutations to 0
    num_good_permutations = 0
    
    # iterate over all permutations of size n
    for perm in itertools.permutations(range(1, n + 1)):
        # convert the permutation to a list of pairs
        perm_pairs = [(pairs[i - 1][0], pairs[i - 1][1]) for i in perm]
        
        # check if the permutation turns the sequence into a good sequence
        if is_good_sequence(perm_pairs):
            num_good_permutations += 1
    
    # return the number of good permutations modulo 998244353
    return num_good_permutations % 998244353

def is_good_sequence(s):
    # check if the sequence is sorted in non-descending order by first elements
    if is_sorted_by_first_elements(s):
        return False
    
    # check if the sequence is sorted in non-descending order by second elements
    if is_sorted_by_second_elements(s):
        return False
    
    # if neither of the above conditions is true, the sequence is good
    return True

def is_sorted_by_first_elements(s):
    # sort the sequence by first elements in non-descending order
    sorted_s = sorted(s, key=lambda x: x[0])
    
    # check if the sorted sequence is the same as the original sequence
    return sorted_s == s

def is_sorted_by_second_elements(s):
    # sort the sequence by second elements in non-descending order
    sorted_s = sorted(s, key=lambda x: x[1])
    
    # check if the sorted sequence is the same as the original sequence
    return sorted_s == s

n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))
print(solve(n, s))

