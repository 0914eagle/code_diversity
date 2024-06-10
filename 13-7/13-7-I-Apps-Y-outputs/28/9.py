
def paint_balls(N, K):
    # Base case: if there is only one ball, there is only one way to paint it
    if N == 1:
        return K
    
    # Recursive case: there are two ways to paint the first ball and then recursively paint the remaining balls
    return K * paint_balls(N-1, K)

def main():
    N, K = map(int, input().split())
    print(paint_balls(N, K))

if __name__ == '__main__':
    main()

