
def split_bacteria(n):
    if n % 2 != 0:
        return -1

    nights = 0
    splits = []
    while n > 1:
        if n % 2 == 0:
            n //= 2
            splits.append(n)
        else:
            return -1
        nights += 1

    return nights, splits

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = split_bacteria(n)
        if result == -1:
            print(-1)
        else:
            nights, splits = result
            print(nights)
            print(" ".join(map(str, splits)))
