
def solve(s):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0

    # Loop through the string
    while i < n:
        # If the current character is not equal to the next character, increment the count and move on
        if s[i] != s[i+1]:
            count += 1
            i += 1
        # If the current character is equal to the next character, delete the contiguous substring
        else:
            count += 1
            # Find the length of the contiguous substring
            length = 1
            while i+length < n and s[i] == s[i+length]:
                length += 1
            # Increment the count by the length of the substring
            count += length
            # Move the index to the end of the substring
            i += length

    return count

def main():
    n = int(input())
    s = input()
    print(solve(s))

if __name__ == '__main__':
    main()

