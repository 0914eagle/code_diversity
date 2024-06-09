
def get_num_ways_to_paint(N, K):
    # Base case: if there is only one ball, there is only one way to paint it
    if N == 1:
        return K
    
    # Recursive case: if there are multiple balls, consider the first ball and the remaining balls
    num_ways = 0
    for color in range(K):
        # Consider the first ball to be painted in the current color
        num_ways += get_num_ways_to_paint(N-1, K)
    
    return num_ways

def main():
    N, K = map(int, input().split())
    print(get_num_ways_to_paint(N, K))

if __name__ == '__main__':
    main()

