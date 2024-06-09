
def can_transform(source, target, queries):
    # Initialize a dictionary to store the results of the queries
    results = {}
    
    # Iterate over the queries
    for query in queries:
        # Extract the indices of the source and target strings
        a, b, c, d = query
        
        # Check if the query is valid
        if a > b or c > d or a < 1 or b > len(source) or c < 1 or d > len(target):
            results[query] = False
            continue
        
        # Initialize the source and target strings
        source_substring = source[a-1:b]
        target_substring = target[c-1:d]
        
        # Check if the source substring is empty
        if source_substring == "":
            results[query] = False
            continue
        
        # Check if the target substring is empty
        if target_substring == "":
            results[query] = True
            continue
        
        # Check if the source substring can be transformed into the target substring
        results[query] = can_transform_substring(source_substring, target_substring)
    
    # Return the results of the queries
    return results

def can_transform_substring(source, target):
    # Base case: if the source substring is empty, return False
    if source == "":
        return False
    
    # Base case: if the source substring is equal to the target substring, return True
    if source == target:
        return True
    
    # Recursive case: if the source substring is not empty and not equal to the target substring, try to transform it
    if source[0] == "A":
        return can_transform_substring(source[1:], target.replace("A", "AB", 1))
    elif source[0] == "B":
        return can_transform_substring(source[1:], target.replace("B", "BC", 1))
    elif source[0] == "C":
        return can_transform_substring(source[1:], target.replace("C", "AC", 1))
    else:
        return False

if __name__ == "__main__":
    source = "AABCCBAAB"
    target = "ABCB"
    queries = [(1, 3, 1, 2), (2, 2, 2, 4), (7, 9, 1, 1), (3, 4, 2, 3), (4, 5, 1, 3)]
    results = can_transform(source, target, queries)
    print("".join(str(int(result)) for result in results.values()))

