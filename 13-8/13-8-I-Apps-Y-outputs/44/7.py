
def is_reachable(n, m, d, c):
    # Initialize the array a as all zeros
    a = [0] * (n + 2)
    
    # Initialize the variables to keep track of the current position and the number of jumps
    curr_pos = 0
    num_jumps = 0
    
    # Loop through each platform
    for i in range(m):
        # Check if the current platform overlaps with the previous platform
        if curr_pos + c[i] > n + 1:
            return False
        
        # Update the array a with the index of the current platform
        for j in range(curr_pos, curr_pos + c[i]):
            a[j] = i + 1
        
        # Update the current position and number of jumps
        curr_pos += c[i]
        num_jumps += 1
    
    # Check if the final position is reachable
    if curr_pos != n + 1:
        return False
    
    # Check if the number of jumps is within the maximum distance
    if num_jumps > d:
        return False
    
    # Check if the array a is valid
    for i in range(1, m):
        if a.count(i) != c[i - 1]:
            return False
    
    return True

def find_solution(n, m, d, c):
    # Initialize the array a as all zeros
    a = [0] * (n + 2)
    
    # Initialize the variables to keep track of the current position and the number of jumps
    curr_pos = 0
    num_jumps = 0
    
    # Loop through each platform
    for i in range(m):
        # Check if the current platform overlaps with the previous platform
        if curr_pos + c[i] > n + 1:
            return False
        
        # Update the array a with the index of the current platform
        for j in range(curr_pos, curr_pos + c[i]):
            a[j] = i + 1
        
        # Update the current position and number of jumps
        curr_pos += c[i]
        num_jumps += 1
    
    # Check if the final position is reachable
    if curr_pos != n + 1:
        return False
    
    # Check if the number of jumps is within the maximum distance
    if num_jumps > d:
        return False
    
    # Check if the array a is valid
    for i in range(1, m):
        if a.count(i) != c[i - 1]:
            return False
    
    return a

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print(is_reachable(n, m, d, c))
    print(*find_solution(n, m, d, c))

