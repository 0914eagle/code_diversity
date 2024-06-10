
import sys

def get_input():
    n = int(input())
    values = list(map(int, input().split()))
    return n, values

def compose_ingredients(values):
    while len(values) > 1:
        values = [sum(values[i:i+2])/2 for i in range(0, len(values), 2)]
    return values[0]

def main():
    n, values = get_input()
    print(compose_ingredients(values))

if __name__ == '__main__':
    main()

