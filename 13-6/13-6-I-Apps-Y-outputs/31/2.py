
def get_min_operations(s, t):
    # Initialize variables
    n = len(s)
    count = 0
    diff = [0] * n

    # Loop through each character of both strings
    for i in range(n):
        # If characters are different, increment count and mark the difference
        if s[i] != t[i]:
            count += 1
            diff[i] = 1

    # If count is 0, no operations needed
    if count == 0:
        return 0

    # If count is 1, only one operation needed
    if count == 1:
        return 1

    # If count is 2, two operations needed
    if count == 2:
        return 2

    # If count is greater than 2, find the minimum number of operations needed
    min_operations = float('inf')
    for i in range(n):
        # If character is different and not marked, try replacing it with a different character
        if diff[i] == 1 and s[i] != t[i]:
            # Replace character with a different character
            diff[i] = 0
            count -= 1

            # Recursively call function to find minimum number of operations needed
            min_operations = min(min_operations, get_min_operations(s, t))

            # Undo replacement
            diff[i] = 1
            count += 1

    return min_operations

def main():
    s = input()
    t = input()
    print(get_min_operations(s, t))

if __name__ == '__main__':
    main()

