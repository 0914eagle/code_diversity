
def get_shifted_string(n, s):
    
    shifted_string = ""
    for char in s:
        shifted_char = chr((ord(char) - ord("A") + n) % 26 + ord("A"))
        shifted_string += shifted_char
    return shifted_string

def main():
    n = int(input())
    s = input()
    shifted_string = get_shifted_string(n, s)
    print(shifted_string)

if __name__ == '__main__':
    main()

