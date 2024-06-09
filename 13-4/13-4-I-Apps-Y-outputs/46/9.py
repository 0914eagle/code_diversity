
def get_input():
    n = int(input())
    s = input()
    return n, s

def shift_char(c, n):
    return chr((ord(c) - ord('A') + n) % 26 + ord('A'))

def shift_string(s, n):
    return ''.join(shift_char(c, n) for c in s)

def main():
    n, s = get_input()
    print(shift_string(s, n))

if __name__ == '__main__':
    main()

