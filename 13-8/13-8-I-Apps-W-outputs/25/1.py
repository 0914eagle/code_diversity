
def solve(n, b):
    # Sort the input array
    b.sort()
    
    # Create a dictionary to store the counts of each element
    counts = {}
    for num in b:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Check if the sequence is strictly increasing
    for i in range(n-1):
        if b[i] >= b[i+1]:
            return "No"
    
    # Check if the sequence can be permutated to be strictly increasing
    for perm in permutations(b):
        # Check if the permutation is valid
        if is_valid_permutation(perm):
            return "Yes\n" + " ".join(map(str, perm))
    
    return "No"

def is_valid_permutation(perm):
    # Check if the permutation is valid by checking if the number of occurrences of each element is the same
    counts = {}
    for num in perm:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num in counts:
        if counts[num] != b.count(num):
            return False
    
    return True

# Test the function with the example input
n = 6
b = [4, 7, 7, 12, 31, 61]
print(solve(n, b))

# Test the function with another example input
n = 3
b = [1, 2, 3]
print(solve(n, b))

