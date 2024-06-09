
def get_good_string(strings):
    # Initialize a dictionary to store the frequency of each substring
    substring_freq = {}
    for string in strings:
        # Iterate over each substring of the current string
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                # Check if the substring is already in the dictionary
                if string[i:j] in substring_freq:
                    # If it is, increment its frequency
                    substring_freq[string[i:j]] += 1
                else:
                    # If it's not, add it to the dictionary with frequency of 1
                    substring_freq[string[i:j]] = 1
    
    # Find the substring with the maximum frequency
    max_freq = max(substring_freq.values())
    good_strings = []
    for substring, freq in substring_freq.items():
        # If the frequency of the substring is equal to the maximum frequency,
        # it is a good substring
        if freq == max_freq:
            good_strings.append(substring)
    
    # If there are no good strings, return "NO"
    if not good_strings:
        return "NO"
    
    # Otherwise, return the lexicographically minimum good string
    return min(good_strings)

def main():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    print(get_good_string(strings))

if __name__ == '__main__':
    main()

