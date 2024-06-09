
def solve(n, k):
    # Check if all elements are already equal to k
    if all(a == k for a in a_list):
        return "yes"
    
    # Check if it is possible to make all elements equal to k in one operation
    if len(set(a_list)) == 1:
        return "no"
    
    # Check if it is possible to make all elements equal to k in two operations
    if len(set(a_list)) == 2:
        if a_list[0] == k or a_list[-1] == k:
            return "yes"
        else:
            return "no"
    
    # Check if it is possible to make all elements equal to k in three or more operations
    for i in range(len(a_list)):
        if a_list[i] != k:
            break
    
    # If all elements are equal to k, return "yes"
    if i == len(a_list) - 1:
        return "yes"
    
    # If it is not possible to make all elements equal to k in three or more operations, return "no"
    return "no"

