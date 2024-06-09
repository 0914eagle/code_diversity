
def get_min_changes(s, k):
    # Initialize variables
    n = len(s)
    changes = 0
    i = 0
    j = 0
    
    # Loop through the string
    while i < n and j < k:
        # If the current character is not 'R', 'G', or 'B', change it to 'R'
        if s[i] not in ["R", "G", "B"]:
            changes += 1
            s = s[:i] + "R" + s[i+1:]
            n += 1
        
        # If the current character is 'R', 'G', or 'B', move on to the next character
        else:
            i += 1
        
        # If the current substring is a substring of the infinite string "RGBRGBRGB ...", move on to the next character
        if s[j:j+k] in ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]:
            j += 1
    
    # Return the minimum number of changes needed
    return changes

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        s = input()
        print(get_min_changes(s, k))

if __name__ == '__main__':
    main()

