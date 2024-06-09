
def get_number_of_ways(N, K):
    # Base case: if N is 1, there is only one way to paint the ball
    if N == 1:
        return K
    
    # Recursive case: if N is greater than 1, there are K ways to paint the first ball
    # and then recursively find the number of ways to paint the remaining balls
    return K * get_number_of_ways(N-1, K)

def main():
    N, K = map(int, input().split())
    print(get_number_of_ways(N, K))

if __name__ == '__main__':
    main()

