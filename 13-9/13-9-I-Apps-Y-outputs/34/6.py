
def number_of_ways_to_paint_balls(N, K):
    if N == 1:
        return K
    if K == 1:
        return 1
    return number_of_ways_to_paint_balls(N-1, K) * (K-1) + number_of_ways_to_paint_balls(N-1, K-1)

def main():
    N, K = map(int, input().split())
    print(number_of_ways_to_paint_balls(N, K))

if __name__ == '__main__':
    main()

