
def number_of_ways_to_paint_balls(n, k):
    if n == 1:
        return k
    if n == 2:
        return k * (k - 1)
    return number_of_ways_to_paint_balls(n - 1, k) * (k - 1) + number_of_ways_to_paint_balls(n - 2, k)

def main():
    n, k = map(int, input().split())
    print(number_of_ways_to_paint_balls(n, k))

if __name__ == '__main__':
    main()

