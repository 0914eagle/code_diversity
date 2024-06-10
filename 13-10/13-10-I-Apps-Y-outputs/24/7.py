
def get_available_data(x, n, spent_data):
    available_data = x
    for i in range(n):
        available_data -= spent_data[i]
        if available_data < 0:
            available_data = 0
    return available_data

def main():
    x = int(input())
    n = int(input())
    spent_data = []
    for i in range(n):
        spent_data.append(int(input()))
    available_data = get_available_data(x, n, spent_data)
    print(available_data)

if __name__ == '__main__':
    main()

