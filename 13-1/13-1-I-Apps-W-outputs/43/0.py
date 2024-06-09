
def brutality(n, k, a, s):
    # Initialize the variables
    dmg = 0
    count = [0] * 26
    skip = [False] * n
    for i in range(n):
        # Check if the button is already broken
        if count[ord(s[i]) - ord('a')] >= k:
            skip[i] = True
            continue
        # Increment the count for the current button
        count[ord(s[i]) - ord('a')] += 1
        # Add the damage to the total damage
        dmg += a[i]
    # Return the total damage
    return dmg

def main():
    # Read the input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    # Calculate the brutality
    dmg = brutality(n, k, a, s)
    # Print the result
    print(dmg)

if __name__ == '__main__':
    main()

