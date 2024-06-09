
def get_available_megabytes(x, n, spent_megabytes):
    available_megabytes = x
    for i in range(n):
        available_megabytes += spent_megabytes[i]
        available_megabytes -= spent_megabytes[i]
    return available_megabytes

def main():
    x = int(input())
    n = int(input())
    spent_megabytes = []
    for i in range(n):
        spent_megabytes.append(int(input()))
    available_megabytes = get_available_megabytes(x, n, spent_megabytes)
    print(available_megabytes)

if __name__ == '__main__':
    main()

