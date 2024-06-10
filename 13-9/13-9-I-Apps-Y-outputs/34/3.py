
def number_of_ways_to_paint_balls(n, k):
    if n == 1:
        return k
    else:
        return (k * number_of_ways_to_paint_balls(n-1, k)) % (10**9 + 7)

def main():
    n, k = map(int, input().split())
    print(number_of_ways_to_paint_balls(n, k))

if __name__ == '__main__':
    main()

