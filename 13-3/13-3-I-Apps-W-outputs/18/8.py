
def get_composite_summands(n):
    summands = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            summands.append(i)
            if n // i != i:
                summands.append(n // i)
    return summands

def get_max_composite_summands(n):
    summands = get_composite_summands(n)
    if len(summands) == 0:
        return -1
    return len(summands)

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        print(get_max_composite_summands(n))

if __name__ == '__main__':
    main()

