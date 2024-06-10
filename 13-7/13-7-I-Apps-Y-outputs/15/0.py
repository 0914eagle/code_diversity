
def get_strings(n, k):
    strings = []
    for i in range(n):
        for j in range(i+1, n):
            strings.append('a' * i + 'b' * (j-i) + 'a' * (n-j))
    return strings[k-1]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(get_strings(n, k))

if __name__ == '__main__':
    main()

