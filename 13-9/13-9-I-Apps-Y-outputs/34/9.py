
def paint_balls(n, k):
    # Base case: if there is only one ball, there is only one way to paint it
    if n == 1:
        return k
    
    # Recursive case: paint the first ball and then paint the rest of the balls
    return k * paint_balls(n-1, k)

def main():
    n, k = map(int, input().split())
    print(paint_balls(n, k))

if __name__ == '__main__':
    main()

