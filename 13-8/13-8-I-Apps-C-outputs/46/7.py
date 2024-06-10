
def get_f(n):
    if n == 0:
        return "What are you doing at the end of the world? Are you busy? Will you save us?"
    else:
        return "What are you doing while sending \"" + get_f(n-1) + "\"? Are you busy? Will you send \"" + get_f(n-1) + "\"?"

def get_character(n, k):
    f = get_f(n)
    if k <= len(f):
        return f[k-1]
    else:
        return '.'

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        print(get_character(n, k), end='')

