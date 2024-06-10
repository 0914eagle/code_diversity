
def get_minimum_time(sticks):
    sticks.sort(reverse=True)
    total_time = 0
    while sticks[0] + sticks[1] <= sticks[2]:
        total_time += 1
        sticks[0] += 1
    return total_time

def main():
    a, b, c = map(int, input().split())
    sticks = [a, b, c]
    print(get_minimum_time(sticks))

if __name__ == '__main__':
    main()

