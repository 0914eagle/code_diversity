
def get_original_string(k, n, strings):
    # Initialize a dictionary to store the frequencies of each character
    char_freq = {}
    for i in range(n):
        char_freq[i] = 0
    
    # Iterate over the strings and increment the frequency of each character
    for string in strings:
        for i in range(n):
            char_freq[i] += string[i]
    
    # Check if the frequency of each character is divisible by k
    for i in range(n):
        if char_freq[i] % k != 0:
            return "-1"
    
    # Initialize the original string
    original_string = ""
    
    # Iterate over the characters and add the most frequent character to the original string
    for i in range(n):
        max_freq = 0
        max_char = ""
        for char in range(n):
            if char_freq[char] > max_freq:
                max_freq = char_freq[char]
                max_char = chr(ord('a') + char)
        original_string += max_char
        char_freq[ord(max_char) - ord('a')] = 0
    
    return original_string

def main():
    k, n = map(int, input().split())
    strings = [input() for _ in range(k)]
    print(get_original_string(k, n, strings))

if __name__ == '__main__':
    main()

