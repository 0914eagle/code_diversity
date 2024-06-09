
def get_max_earned(a):
    # Initialize variables
    n = len(a)
    multiples = []
    earnings = 0

    # Find all multiples of x
    for i in range(1, n + 1):
        if i in multiples:
            continue
        for j in range(i, n + 1, i):
            if j not in multiples:
                multiples.append(j)

    # Calculate earnings
    for i in range(1, n + 1):
        if i not in multiples:
            earnings += a[i - 1]

    return earnings

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_earned(a))

if __name__ == '__main__':
    main()

