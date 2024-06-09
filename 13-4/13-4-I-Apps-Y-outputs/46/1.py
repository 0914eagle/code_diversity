
def get_shifted_string(s, n):
    # Create a dictionary to map each character to its shifted character
    char_map = {}
    for i in range(26):
        char_map[chr(i + ord('A'))] = chr((i + n) % 26 + ord('A'))
    
    # Use the dictionary to shift each character in the string
    shifted_string = ""
    for char in s:
        shifted_string += char_map[char]
    
    return shifted_string

def main():
    n = int(input())
    s = input()
    print(get_shifted_string(s, n))

if __name__ == '__main__':
    main()

