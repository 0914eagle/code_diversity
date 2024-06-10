
def get_available_mb(x, n, monthly_usage):
    available_mb = x
    for i in range(n):
        available_mb -= monthly_usage[i]
        if available_mb < 0:
            available_mb = 0
    return available_mb

def main():
    x = int(input())
    n = int(input())
    monthly_usage = []
    for i in range(n):
        monthly_usage.append(int(input()))
    available_mb = get_available_mb(x, n, monthly_usage)
    print(available_mb)

if __name__ == '__main__':
    main()

