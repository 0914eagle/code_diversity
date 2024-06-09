
def get_substring(s, k):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0
    j = 0
    
    # Loop through the string
    while i < n and j < k:
        # If the current character is not 'R', 'G', or 'B', skip it
        if s[i] not in ["R", "G", "B"]:
            i += 1
            continue
        
        # If the current character is 'R', 'G', or 'B', check if it is part of the substring
        if s[i] == "R":
            if j == 0 or s[i-1] != "R":
                count += 1
                j += 1
        elif s[i] == "G":
            if j == 0 or s[i-1] != "G":
                count += 1
                j += 1
        elif s[i] == "B":
            if j == 0 or s[i-1] != "B":
                count += 1
                j += 1
        
        # If the substring is found, return the count
        if j == k:
            return count
        
        # Increment the index
        i += 1
    
    # If the substring is not found, return -1
    return -1

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        s = input()
        print(get_substring(s, k))

if __name__ == '__main__':
    main()

