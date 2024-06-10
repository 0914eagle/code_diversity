
def get_available_megabytes(x, n, spendings):
    available_megabytes = x
    for i in range(n):
        available_megabytes += spendings[i]
        available_megabytes -= x
    return available_megabytes

def main():
    x = int(input())
    n = int(input())
    spendings = []
    for i in range(n):
        spendings.append(int(input()))
    available_megabytes = get_available_megabytes(x, n, spendings)
    print(available_megabytes)

if __name__ == '__main__':
    main()

