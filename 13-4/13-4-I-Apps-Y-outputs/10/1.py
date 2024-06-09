
def get_available_megabytes(x, n, months_spent):
    available_megabytes = x
    for i in range(n):
        available_megabytes += months_spent[i]
    return available_megabytes

def main():
    x = int(input())
    n = int(input())
    months_spent = []
    for i in range(n):
        months_spent.append(int(input()))
    available_megabytes = get_available_megabytes(x, n, months_spent)
    print(available_megabytes)

if __name__ == '__main__':
    main()

