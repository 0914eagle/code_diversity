
def get_min_moves(a, k):
    # Initialize variables
    n = len(a)
    x = 0
    moves = 0
    visited = [False] * n

    # Loop through each element of the array
    for i in range(n):
        # If the element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1

        # If the element is divisible by k, mark it as visited
        else:
            visited[i] = True

    # Loop through each element of the array again
    for i in range(n):
        # If the element is not visited and not divisible by k, add x to it and increase x by 1
        if not visited[i] and a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1

    # Return the minimum number of moves required to obtain an array where each element is divisible by k
    return moves

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_min_moves(a, k))

if __name__ == '__main__':
    main()

