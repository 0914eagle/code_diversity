
def is_power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)

def get_min_days(n):
    if n == 1:
        return 0
    if is_power_of_two(n):
        return 1
    for i in range(2, n):
        if is_power_of_two(i) and is_power_of_two(n - i):
            return 2
    return -1

def get_split_counts(n):
    if n == 1:
        return [0]
    if is_power_of_two(n):
        return [1]
    for i in range(2, n):
        if is_power_of_two(i) and is_power_of_two(n - i):
            return [i // 2, (n - i) // 2]
    return []

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        min_days = get_min_days(n)
        if min_days == -1:
            print(-1)
        else:
            split_counts = get_split_counts(n)
            print(min_days)
            print(" ".join(str(x) for x in split_counts))

if __name__ == '__main__':
    main()

