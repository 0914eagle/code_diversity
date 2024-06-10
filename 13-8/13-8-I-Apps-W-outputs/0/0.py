
def get_charges(n):
    return list(map(int, input().split()))

def synchronize(charges):
    n = len(charges)
    for i in range(1, n - 1):
        charges[i] = charges[i + 1] + charges[i - 1] - charges[i]
    return charges

def is_possible(charges1, charges2):
    return all(c1 == c2 for c1, c2 in zip(charges1, synchronize(charges2)))

def main():
    n = int(input())
    charges1 = get_charges(n)
    charges2 = get_charges(n)
    print("Yes") if is_possible(charges1, charges2) else print("No")

if __name__ == '__main__':
    main()

