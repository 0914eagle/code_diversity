
import math

def get_diagonals(N):
    # Calculate the diagonals of the polygon
    diagonals = []
    for i in range(N):
        for j in range(i+1, N):
            diagonals.append((i, j))
    return diagonals

def count_intersections(diagonals):
    # Count the number of intersections between pairs of diagonals
    count = 0
    for i in range(len(diagonals)):
        for j in range(i+1, len(diagonals)):
            d1 = diagonals[i]
            d2 = diagonals[j]
            if d1[0] == d2[0] or d1[0] == d2[1] or d1[1] == d2[0] or d1[1] == d2[1]:
                count += 1
    return count

def main():
    N = int(input())
    diagonals = get_diagonals(N)
    print(count_intersections(diagonals))

if __name__ == '__main__':
    main()

