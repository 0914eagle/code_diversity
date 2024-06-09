
def paint_balls(N, K):
    if N == 1:
        return K
    if K == 1:
        return 1
    return paint_balls(N-1, K-1) + paint_balls(N-1, K)

def main():
    N, K = map(int, input().split())
    print(paint_balls(N, K))

if __name__ == '__main__':
    main()

