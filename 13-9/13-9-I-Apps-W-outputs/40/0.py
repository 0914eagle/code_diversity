
def get_min_time(sticks):
    sticks.sort(reverse=True)
    min_time = 0
    while sticks[0] < sticks[1] + sticks[2]:
        min_time += 1
        sticks[0] += 1
    return min_time

def main():
    a, b, c = map(int, input().split())
    sticks = [a, b, c]
    print(get_min_time(sticks))

if __name__ == '__main__':
    main()

