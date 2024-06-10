
import sys
import math

def get_input():
    N = int(input())
    values = []
    for i in range(N):
        values.append(int(input()))
    return N, values

def compose_ingredients(values):
    while len(values) > 1:
        value1 = values.pop()
        value2 = values.pop()
        values.append((value1 + value2) / 2)
    return values[0]

def get_max_value(values):
    return max(values)

def main():
    N, values = get_input()
    result = compose_ingredients(values)
    print(get_max_value(result))

if __name__ == '__main__':
    main()

