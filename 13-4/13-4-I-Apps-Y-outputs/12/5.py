
import math

def get_volume(length, width, height):
    return length * width * height

def get_max_volume(L):
    volume = 0
    for length in range(1, L + 1):
        for width in range(1, L + 1):
            for height in range(1, L + 1):
                if length + width + height == L:
                    volume = max(volume, get_volume(length, width, height))
    return volume

def main():
    L = int(input())
    print(get_max_volume(L))

if __name__ == '__main__':
    main()

