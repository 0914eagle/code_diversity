
def can_fold(arr):
    # Check if the input array is valid
    if len(arr) != 6 or len(arr[0]) != 6:
        return "Invalid input"
    
    # Check if the input array contains only . and #
    for row in arr:
        for char in row:
            if char not in [".", "#"]:
                return "Invalid input"
    
    # Check if the input array is connected
    visited = set()
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if arr[row][col] == "#":
            queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])
    
    if len(visited) != 6:
        return "Cannot fold"
    
    # Check if the input array contains a 2x2 square of #
    for row in range(4):
        for col in range(4):
            if arr[row][col] == "#" and arr[row+1][col] == "#" and arr[row][col+1] == "#" and arr[row+1][col+1] == "#":
                return "Cannot fold"
    
    # If all checks pass, the input array can be folded into a cube
    return "Can fold"

def main():
    arr = [
        input(),
        input(),
        input(),
        input(),
        input(),
        input()
    ]
    print(can_fold(arr))

if __name__ == '__main__':
    main()

