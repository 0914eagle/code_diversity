nstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i] - 1] = i + 1
    return arrows

if __name__ == "__main__":
    N, K = map(int, input().split())
    dancers = list(map(int, input().split()))
    
    result = reconstruct_arrows(N, K, dancers)
    if result.count(0) > 0:
        print("Impossible")
    else:
        print(*result)
