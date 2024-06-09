
def get_good_string(strings):
    # Initialize a dictionary to store the frequency of each substring
    substring_freq = {}
    for string in strings:
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                if substring not in substring_freq:
                    substring_freq[substring] = 1
                else:
                    substring_freq[substring] += 1
    
    # Find the most frequent substring
    most_frequent_substring = ""
    most_frequent_substring_freq = 0
    for substring, freq in substring_freq.items():
        if freq > most_frequent_substring_freq:
            most_frequent_substring = substring
            most_frequent_substring_freq = freq
    
    # Check if all strings are the most frequent substring
    for string in strings:
        if most_frequent_substring not in string:
            return "NO"
    
    # Find the lexicographically minimum string with the most frequent substring
    min_string = ""
    for string in strings:
        if string.startswith(most_frequent_substring):
            if min_string == "":
                min_string = string
            elif string < min_string:
                min_string = string
    
    return min_string

def main():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    print(get_good_string(strings))

if __name__ == '__main__':
    main()

