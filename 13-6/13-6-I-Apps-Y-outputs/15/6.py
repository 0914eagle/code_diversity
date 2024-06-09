
def get_liked_foods(N, M, A):
    liked_foods = set(A[0])
    for i in range(1, N):
        liked_foods &= set(A[i])
    return len(liked_foods)

