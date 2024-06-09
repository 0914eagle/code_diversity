
def get_input():
    N = int(input())
    S = input()
    return N, S

def shift_char(c, n):
    return chr((ord(c) - ord('A') + n) % 26 + ord('A'))

def shift_string(S, n):
    return ''.join([shift_char(c, n) for c in S])

def main():
    N, S = get_input()
    print(shift_string(S, N))

if __name__ == '__main__':
    main()

