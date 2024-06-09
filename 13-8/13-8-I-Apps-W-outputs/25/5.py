
def solve(b):
    n = len(b)
    # Create a dictionary to store the number of occurrences of each element in b
    count = {}
    for i in range(n):
        if b[i] in count:
            count[b[i]] += 1
        else:
            count[b[i]] = 1
    
    # Sort the dictionary by value in descending order
    count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    
    # Create a list to store the permutation
    perm = []
    
    # Add the elements to the permutation list
    for i in range(n):
        perm.append(list(count.keys())[i])
    
    return "Yes\n" + " ".join(map(str, perm))

