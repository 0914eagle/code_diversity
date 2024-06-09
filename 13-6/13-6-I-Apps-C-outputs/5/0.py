
def f(string):
    # Your code here
    return string

def main():
    S = input()
    T = [input() for _ in range(13)]
    K = int(input())
    M = int(input())
    m = [int(i) for i in input().split()]

    password = S
    for i in range(K):
        password = f(password)

    for i in range(M):
        print(password[m[i] - 1])

if __name__ == '__main__':
    main()

