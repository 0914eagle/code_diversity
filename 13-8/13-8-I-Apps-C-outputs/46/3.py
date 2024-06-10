
def solve(f_n, k):
    if k == 0:
        return '.'
    if k == 1:
        return f_n[0]
    return solve(f_n[1:], k-1)

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        f_n = "What are you doing at the end of the world? Are you busy? Will you save us?"
        for i in range(n):
            f_n = "What are you doing while sending \"" + f_n + "\"? Are you busy? Will you send \"" + f_n + "\"?"
        print(solve(f_n, k))

if __name__ == '__main__':
    main()

