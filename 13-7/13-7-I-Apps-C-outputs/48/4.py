
def is_possible(q, s, k):
    n = len(q)
    board = [i for i in range(1, n+1)]
    for i in range(k):
        if q[i-1] != s[i-1]:
            board = apply_permutation(board, q[i-1])
    return board == s

def apply_permutation(board, permutation):
    n = len(board)
    new_board = [0] * n
    for i in range(n):
        new_board[permutation-1] = board[i]
        permutation = (permutation + 1) % n
    return new_board

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print("YES") if is_possible(q, s, k) else print("NO")

