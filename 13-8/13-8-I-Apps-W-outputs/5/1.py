
def get_input():
    N = int(input())
    T = input()
    return N, T

def count_occurrences(T, S):
    count = 0
    for i in range(len(S) - len(T) + 1):
        if S[i:i+len(T)] == T:
            count += 1
    return count

def main():
    N, T = get_input()
    S = "110" * 10**10
    print(count_occurrences(T, S))

if __name__ == '__main__':
    main()

