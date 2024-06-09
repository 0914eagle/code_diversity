
def can_obtain_target_string(source, target, queries):
    # Initialize a dictionary to store the results of the queries
    results = {}
    
    # Iterate over the queries
    for query in queries:
        # Extract the indices of the source and target strings
        start_source, end_source, start_target, end_target = query
        
        # Check if the source string can be transformed into the target string
        results[query] = can_transform_string(source[start_source - 1:end_source], target[start_target - 1:end_target])
    
    # Return the results of the queries
    return results

def can_transform_string(source, target):
    # Base case: if the source string is empty, return True if the target string is also empty
    if not source:
        return not target
    
    # Base case: if the target string is empty, return False
    if not target:
        return False
    
    # Check if the first character of the source string matches the first character of the target string
    if source[0] == target[0]:
        # If they match, recursively check if the remaining characters of the source string can be transformed into the remaining characters of the target string
        return can_transform_string(source[1:], target[1:])
    
    # Check if the first character of the source string is 'A' and the first character of the target string is 'B'
    if source[0] == 'A' and target[0] == 'B':
        # If they match, recursively check if the remaining characters of the source string can be transformed into the remaining characters of the target string
        return can_transform_string(source[1:], target[1:])
    
    # Check if the first character of the source string is 'B' and the first character of the target string is 'A'
    if source[0] == 'B' and target[0] == 'A':
        # If they match, recursively check if the remaining characters of the source string can be transformed into the remaining characters of the target string
        return can_transform_string(source[1:], target[1:])
    
    # Check if the first character of the source string is 'C' and the first character of the target string is 'A'
    if source[0] == 'C' and target[0] == 'A':
        # If they match, recursively check if the remaining characters of the source string can be transformed into the remaining characters of the target string
        return can_transform_string(source[1:], target[1:])
    
    # If none of the above conditions are met, return False
    return False

if __name__ == '__main__':
    source = input()
    target = input()
    queries = []
    
    for _ in range(int(input())):
        queries.append(list(map(int, input().split())))
    
    results = can_obtain_target_string(source, target, queries)
    
    for query, result in results.items():
        print('1' if result else '0')

