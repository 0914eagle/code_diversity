
def find_longest_repeated_substring(string):
    # find all repeated substrings
    repeated_substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j+1]
            if substring in string[:i] or substring in string[j+1:]:
                repeated_substrings.append(substring)
    
    # find the longest repeated substring
    longest_substring = ""
    for substring in repeated_substrings:
        if len(substring) > len(longest_substring):
            longest_substring = substring
    
    return longest_substring

def main():
    string = input("Enter a string of lowercase letters: ")
    repeated_substring = find_longest_repeated_substring(string)
    print(f"The longest repeated substring is: {repeated_substring}")

if __name__ == '__main__':
    main()

