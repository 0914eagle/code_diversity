
def get_max_coins(A, B):
    return max(A + (A - 1), A + B)

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(get_max_coins(A, B))
