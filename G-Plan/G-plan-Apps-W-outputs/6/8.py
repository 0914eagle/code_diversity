
def can_transform_matrix(A, B):
    n = len(A)
    m = len(A[0])
    
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                if i < n - 1 and j < m - 1:
                    A[i][j] = 1 - A[i][j]
                    A[i+1][j] = 1 - A[i+1][j]
                    A[i][j+1] = 1 - A[i][j+1]
                    A[i+1][j+1] = 1 - A[i+1][j+1]
                else:
                    return "No"
    
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(n)]
    
    result = can_transform_matrix(A, B)
    print(result)
