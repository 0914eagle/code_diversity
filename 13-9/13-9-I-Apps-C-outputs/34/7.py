
def longest_repeated_substring(input_string):
    # find all occurrences of the substring
    occurrences = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substring = input_string[i:j]
            if substring in input_string[j:]:
                occurrences.append(substring)
    
    # find the longest repeated substring
    longest_substring = ""
    for substring in occurrences:
        if len(substring) > len(longest_substring):
            longest_substring = substring
    
    return longest_substring

def main():
    input_string = input()
    longest_substring = longest_repeated_substring(input_string)
    print(longest_substring)

if __name__ == '__main__':
    main()

