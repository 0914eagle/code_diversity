
def solve(b):
    n = len(b)
    # Convert the list of integers to a set to remove duplicates
    b_set = set(b)
    # Create a dictionary to map each integer to its count in the list
    count = {x: b.count(x) for x in b_set}
    # Sort the dictionary by value in descending order
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    # Initialize an empty list to store the permutation
    permutation = []
    # Loop through the sorted dictionary and add the integers to the permutation
    for item in sorted_count:
        permutation += [item[0]] * item[1]
    # Check if the permutation is valid by ensuring that the sequence is strictly increasing
    if sorted(permutation) == list(range(1, n + 1)):
        return "Yes\n" + " ".join(str(x) for x in permutation)
    else:
        return "No"

