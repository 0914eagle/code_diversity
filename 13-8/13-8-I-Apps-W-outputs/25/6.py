
def solve(n, b):
    # Convert the list of integers to a set to remove duplicates
    b_set = set(b)
    # Initialize a dictionary to store the count of each integer
    count = {}
    for i in b_set:
        count[i] = b.count(i)
    
    # Sort the dictionary by value in descending order
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize an empty list to store the permutation
    permutation = []
    
    # Iterate through the sorted dictionary and add the integers to the permutation
    for i in sorted_count:
        permutation += [i[0]] * i[1]
    
    # Check if the permutation is valid by checking if the sequence is strictly increasing
    if is_strictly_increasing(permutation):
        return "Yes\n" + " ".join(map(str, permutation))
    
    return "No"

def is_strictly_increasing(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True

n = int(input())
b = list(map(int, input().split()))
print(solve(n, b))

