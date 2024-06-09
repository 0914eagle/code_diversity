
def get_good_string(strings):
    # Step 1: Find the most frequent substring in the set of strings
    freq = {}
    for string in strings:
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                if substring not in freq:
                    freq[substring] = 1
                else:
                    freq[substring] += 1
    most_freq_substring = max(freq, key=freq.get)

    # Step 2: Find all good strings in the set of strings
    good_strings = []
    for string in strings:
        if most_freq_substring in string:
            good_strings.append(string)

    # Step 3: Return the lexicographically minimum good string with minimum length
    if len(good_strings) == 0:
        return "NO"
    else:
        return min(good_strings)

if __name__ == '__main__':
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    print(get_good_string(strings))

