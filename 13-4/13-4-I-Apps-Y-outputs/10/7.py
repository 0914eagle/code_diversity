
def get_available_mb(x, n, p):
    available_mb = x
    for i in range(n):
        available_mb -= p[i]
        if available_mb < 0:
            available_mb = 0
    return available_mb

def main():
    x = int(input())
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    available_mb = get_available_mb(x, n, p)
    print(available_mb)

if __name__ == '__main__':
    main()

