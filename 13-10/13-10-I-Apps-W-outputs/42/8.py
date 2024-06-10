
def get_periods(a, b):
    periods = set()
    for i in range(1, a+b+1):
        period = i
        s = "A" * a + "B" * b
        while len(s) % period != 0:
            s += s
        periods.add(period)
    return len(periods)

def main():
    a, b = map(int, input().split())
    print(get_periods(a, b))

if __name__ == '__main__':
    main()

