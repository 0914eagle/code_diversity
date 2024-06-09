
def solve(n, b):
    # Convert the list of integers to a set to remove duplicates
    b_set = set(b)
    # Initialize a dictionary to store the count of each integer
    count = {}
    for i in b_set:
        count[i] = b.count(i)
    
    # Sort the dictionary by value in descending order
    count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    
    # Initialize an empty list to store the permutation
    permutation = []
    
    # Iterate through the dictionary and add the integers to the permutation
    for i in count:
        permutation += [i] * count[i]
    
    # Check if the permutation is strictly increasing
    for i in range(1, n):
        if permutation[i] <= permutation[i-1]:
            return "No"
    
    return "Yes\n" + " ".join(str(i) for i in permutation)

