
def get_max_strength(n, p, assignment):
    # Initialize the maximum strength and the suffix to flip
    max_strength = 0
    suffix_to_flip = ""
    
    # Iterate over all possible suffixes of length 1 to n-1
    for i in range(1, n):
        # Get the strength of the pieces in the suffix
        suffix_strength = sum(p[j] for j in range(n-i, n))
        
        # If the suffix strength is greater than the current maximum strength, update the maximum strength and the suffix to flip
        if suffix_strength > max_strength:
            max_strength = suffix_strength
            suffix_to_flip = assignment[n-i:]
    
    # Return the maximum strength and the suffix to flip
    return max_strength, suffix_to_flip

def solve(n, p, assignment):
    # Get the maximum strength and the suffix to flip
    max_strength, suffix_to_flip = get_max_strength(n, p, assignment)
    
    # Initialize the updated assignment
    updated_assignment = assignment
    
    # If the suffix to flip is not empty, flip the characters in the suffix
    if suffix_to_flip != "":
        for i in range(len(suffix_to_flip)):
            if suffix_to_flip[i] == "A":
                updated_assignment = updated_assignment[:n-i-1] + "B" + updated_assignment[n-i:]
            else:
                updated_assignment = updated_assignment[:n-i-1] + "A" + updated_assignment[n-i:]
    
    # Return the maximum strength and the updated assignment
    return max_strength, updated_assignment

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()
    max_strength, updated_assignment = solve(n, p, assignment)
    print(max_strength)

