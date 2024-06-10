
def find_nesting(corner_pairs):
    # Initialize a dictionary to store the nesting structure
    nesting = {}

    # Loop through each corner pair
    for i, (r1, c1) in enumerate(corner_pairs):
        # Find the corresponding bottom-right corner
        for j, (r2, c2) in enumerate(corner_pairs):
            if r1 == r2 and c1 == c2:
                # If the corners are the same, they are part of the same rectangle
                nesting[i] = j
                break
        else:
            # If no matching bottom-right corner is found, the rectangle is invalid
            return "syntax error"

    # Check if the nesting structure is valid
    if not is_valid_nesting(nesting, len(corner_pairs)):
        return "syntax error"

    # Return the nesting structure
    return nesting

def is_valid_nesting(nesting, n):
    # Initialize a set to store the visited corners
    visited = set()

    # Loop through each corner
    for i in range(n):
        # If the corner has already been visited, the nesting structure is invalid
        if i in visited:
            return False
        # Mark the corner as visited
        visited.add(i)
        # If the corner has a parent, mark its parent as visited too
        if i in nesting:
            visited.add(nesting[i])

    # If all corners have been visited, the nesting structure is valid
    return len(visited) == n

def main():
    n = int(input())
    corner_pairs = []
    for i in range(n):
        r, c = map(int, input().split())
        corner_pairs.append((r, c))
    nesting = find_nesting(corner_pairs)
    if nesting == "syntax error":
        print(nesting)
    else:
        print(*nesting.values())

if __name__ == '__main__':
    main()

