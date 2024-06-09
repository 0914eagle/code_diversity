
def f(string, k):
    # Apply the function f k times to the string
    for i in range(k):
        string = apply_f(string)
    return string

def apply_f(string):
    # Apply the function f to the string
    result = ""
    for char in string:
        result += T[ord(char) - ord('a')]
    return result

def main():
    S = input()
    T = [input() for _ in range(13)]
    K = int(input())
    M = int(input())
    m = [int(i) for i in input().split()]

    # Apply the function f K times to S
    password = f(S, K)

    # Print the forgotten letters
    for i in range(M):
        print(password[m[i] - 1])

if __name__ == '__main__':
    main()

