
def get_min_moves(a, k):
    # Initialize variables
    n = len(a)
    x = 0
    moves = 0
    visited = [False] * n
    
    # Loop through each element of the array
    for i in range(n):
        # If the element is not divisible by k, increase x by 1 and add it to the element
        if a[i] % k != 0:
            a[i] += x + 1
            x += 1
            moves += 1
            visited[i] = True
    
    # If all elements are divisible by k, return the minimum number of moves
    if all(a[i] % k == 0 for i in range(n)):
        return moves
    
    # If not all elements are divisible by k, try adding x to each unvisited element and see if it becomes divisible by k
    for i in range(n):
        if not visited[i]:
            a[i] += x
            if a[i] % k == 0:
                moves += 1
                visited[i] = True
    
    # If all elements are divisible by k, return the minimum number of moves
    if all(a[i] % k == 0 for i in range(n)):
        return moves
    
    # If not all elements are divisible by k, try adding x to each unvisited element and see if it becomes divisible by k
    for i in range(n):
        if not visited[i]:
            a[i] += x
            if a[i] % k == 0:
                moves += 1
                visited[i] = True
    
    # Return the minimum number of moves
    return moves

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_min_moves(a, k))

if __name__ == '__main__':
    main()

