
def get_input():
    n = int(input())
    balls = list(map(int, input().split()))
    k = int(input())
    no_neighbors = list(map(int, input().split()))
    l = int(input())
    favorite_sequence = list(map(int, input().split()))
    return n, balls, k, no_neighbors, l, favorite_sequence

def count_arrangements(n, balls, k, no_neighbors, l, favorite_sequence):
    # Initialize a list to store the number of arrangements for each ball
    arrangements = [1] * n
    # Iterate over the no_neighbors list and update the arrangements list
    for i in range(k):
        color = no_neighbors[i]
        for j in range(n):
            if j % color == 0:
                arrangements[j] *= balls[j]
            else:
                arrangements[j] *= (balls[j] - 1)
    # Iterate over the favorite_sequence list and update the arrangements list
    for i in range(l):
        color = favorite_sequence[i]
        arrangements[color-1] *= balls[color-1]
    # Calculate the total number of arrangements
    total_arrangements = 1
    for i in range(n):
        total_arrangements *= arrangements[i]
    return total_arrangements % 1000000007

def main():
    n, balls, k, no_neighbors, l, favorite_sequence = get_input()
    print(count_arrangements(n, balls, k, no_neighbors, l, favorite_sequence))

if __name__ == '__main__':
    main()

