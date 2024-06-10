
def get_available_megabytes(x, n, spent_mb):
    available_mb = x
    for i in range(n):
        available_mb += spent_mb[i]
        available_mb -= x
    return available_mb

def main():
    x = int(input())
    n = int(input())
    spent_mb = []
    for i in range(n):
        spent_mb.append(int(input()))
    available_mb = get_available_megabytes(x, n, spent_mb)
    print(available_mb)

if __name__ == '__main__':
    main()

