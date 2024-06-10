
import math

def read_input():
    N, L, W = map(int, input().split())
    positions = []
    for _ in range(N):
        positions.append(int(input()))
    return N, L, W, positions

def calculate_distance(position, width):
    return math.sqrt(position**2 + width**2)

def move_trees(positions, width):
    distances = [calculate_distance(position, width) for position in positions]
    return sum(distances)

def main():
    N, L, W, positions = read_input()
    print(move_trees(positions, W))

if __name__ == '__main__':
    main()

