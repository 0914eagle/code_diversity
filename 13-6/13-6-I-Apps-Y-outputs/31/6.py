
def get_minimum_operations(s, t):
    # Initialize a dictionary to store the number of operations required for each character
    char_count = {}
    for char in s:
        char_count[char] = 0
    
    # Iterate through the characters of both strings and increment the operation count for each character that is different
    for i in range(len(s)):
        if s[i] != t[i]:
            char_count[s[i]] += 1
    
    # Find the minimum operation count across all characters
    min_operations = min(char_count.values())
    
    return min_operations

def main():
    s = input()
    t = input()
    print(get_minimum_operations(s, t))

if __name__ == '__main__':
    main()

