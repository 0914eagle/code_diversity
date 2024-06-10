
def split_bacteria(n):
    if n % 2 != 0:
        return -1

    nights = 0
    splits = []
    while n > 1:
        if n % 2 == 0:
            splits.append(n // 2)
            n = n // 2
        else:
            splits.append((n // 2) + 1)
            n = (n // 2) + 1
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
            print(" ".join(str(x) for x in splits))
