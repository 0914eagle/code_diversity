
import math

def distance(W):
    # Calculate the distance between Agneta and Beata after W seconds
    distance = math.sin(W)
    return distance

def main():
    W = float(input())
    print(distance(W))

if __name__ == '__main__':
    main()

