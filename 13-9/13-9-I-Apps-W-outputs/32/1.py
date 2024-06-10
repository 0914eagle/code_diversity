
import sys

def get_bouquets(n, a, b):
    # Calculate the number of bouquets that Akari can make
    num_bouquets = 0
    for i in range(1, n+1):
        if i != a and i != b:
            num_bouquets += 1
    
    return num_bouquets

def main():
    n, a, b = map(int, input().split())
    print(get_bouquets(n, a, b))

if __name__ == '__main__':
    main()

