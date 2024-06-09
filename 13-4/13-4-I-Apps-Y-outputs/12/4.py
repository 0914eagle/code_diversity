
import math

def get_input():
    return int(input())

def solve(L):
    max_volume = 0
    for a in range(1, L + 1):
        for b in range(1, L + 1):
            for c in range(1, L + 1):
                if a + b + c == L:
                    volume = a * b * c
                    if volume > max_volume:
                        max_volume = volume
    return max_volume

def main():
    L = get_input()
    print(solve(L))

if __name__ == '__main__':
    main()

