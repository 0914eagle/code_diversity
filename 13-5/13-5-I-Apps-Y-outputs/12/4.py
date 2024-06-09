
from collections import namedtuple

def get_data(n):
    columns = input().split()
    data = []
    for _ in range(n):
        row = namedtuple('Row', columns)(*input().split())
        data.append(row)
    return data

def get_average(data):
    total = 0
    for row in data:
        total += int(row.MARKS)
    return total / len(data)

def main():
    n = int(input())
    data = get_data(n)
    average = get_average(data)
    print(f'{average:.2f}')

if __name__ == '__main__':
    main()

