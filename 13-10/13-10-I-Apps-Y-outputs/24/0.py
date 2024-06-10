
def get_available_megabytes(x, n, data_spent):
    available_megabytes = x
    for i in range(n):
        available_megabytes -= data_spent[i]
        if available_megabytes < 0:
            available_megabytes = 0
    return available_megabytes

def main():
    x = int(input())
    n = int(input())
    data_spent = [int(input()) for _ in range(n)]
    available_megabytes = get_available_megabytes(x, n, data_spent)
    print(available_megabytes)

if __name__ == '__main__':
    main()

