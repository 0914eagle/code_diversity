
def shift_char(char, n):
    return chr((ord(char) - ord('A') + n) % 26 + ord('A'))

def shift_string(s, n):
    return ''.join(shift_char(c, n) for c in s)

def main():
    n = int(input())
    s = input()
    print(shift_string(s, n))

if __name__ == '__main__':
    main()

