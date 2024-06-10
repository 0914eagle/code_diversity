
def get_input():
    N = int(input())
    S = input()
    return N, S

def get_max_different_letters(S):
    N = len(S)
    max_different_letters = 0
    for i in range(N-1):
        X = S[:i+1]
        Y = S[i+1:]
        different_letters = len(set(X).intersection(set(Y)))
        if different_letters > max_different_letters:
            max_different_letters = different_letters
    return max_different_letters

def main():
    N, S = get_input()
    print(get_max_different_letters(S))

if __name__ == '__main__':
    main()

