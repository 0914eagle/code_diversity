
def get_original_string(k, n, strings):
    # Initialize a dictionary to store the frequency of each character in the strings
    char_freq = {}
    for string in strings:
        for char in string:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1
    
    # Check if the frequency of each character is divisible by k
    for char, freq in char_freq.items():
        if freq % k != 0:
            return "-1"
    
    # Initialize an array to store the original string
    original_string = [""] * n
    
    # Fill in the array with the characters from the strings
    for i in range(k):
        for j in range(n):
            original_string[j] += strings[i][j]
    
    return "".join(original_string)

def main():
    k, n = map(int, input().split())
    strings = [input() for _ in range(k)]
    print(get_original_string(k, n, strings))

if __name__ == '__main__':
    main()

