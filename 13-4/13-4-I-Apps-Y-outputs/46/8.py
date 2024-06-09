
def get_input():
    N = int(input())
    S = input()
    return N, S

def shift_char(char, N):
    if char.isalpha():
        new_char = chr((ord(char) - ord('A') + N) % 26 + ord('A'))
    else:
        new_char = char
    return new_char

def shift_string(S, N):
    return ''.join([shift_char(char, N) for char in S])

def main():
    N, S = get_input()
    print(shift_string(S, N))

if __name__ == '__main__':
    main()

