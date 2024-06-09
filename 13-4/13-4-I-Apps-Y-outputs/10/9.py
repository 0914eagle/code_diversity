
def get_available_mb(x, n, months_spent):
    available_mb = x
    for month in months_spent:
        available_mb -= month
        if available_mb < 0:
            available_mb = 0
    return available_mb

def main():
    x = int(input())
    n = int(input())
    months_spent = []
    for i in range(n):
        months_spent.append(int(input()))
    available_mb = get_available_mb(x, n, months_spent)
    print(available_mb)

if __name__ == '__main__':
    main()

