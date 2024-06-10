
def is_possible(q, s, k):
    n = len(q)
    if n != len(s):
        return "NO"
    if k < 0 or k > n:
        return "NO"
    
    # Initialize the board with the permutation q
    board = list(q)
    
    # Perform k moves
    for i in range(k):
        # Toss a coin
        if random.randint(0, 1) == 0:
            # Apply permutation q to the board
            board = [board[i-1] for i in q]
        else:
            # Apply the inverse of permutation q to the board
            board = [board[i-1] for i in range(1, n+1) if i not in q]
            board += [board[i-1] for i in q]
    
    # Check if the final board contains Masha's permutation s
    if board == s:
        return "YES"
    else:
        return "NO"

def main():
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print(is_possible(q, s, k))

if __name__ == '__main__':
    main()

