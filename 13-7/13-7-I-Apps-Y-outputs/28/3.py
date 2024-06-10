
def paint_balls(N, K):
    # Base case: if there are no balls, there is only one way to paint them
    if N == 0:
        return 1
    
    # Recursive case: if there is at least one ball, there are K ways to paint the first ball
    # and then recursively find the number of ways to paint the remaining balls
    return K * paint_balls(N-1, K)

def main():
    N, K = map(int, input().split())
    print(paint_balls(N, K))

if __name__ == '__main__':
    main()

