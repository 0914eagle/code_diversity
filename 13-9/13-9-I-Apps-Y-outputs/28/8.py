
def get_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

def is_second_smallest(p, i):
    if i == 0:
        return p[i + 1] < p[i]
    elif i == len(p) - 1:
        return p[i - 1] < p[i]
    else:
        return p[i - 1] < p[i] and p[i] < p[i + 1]

def count_second_smallest(p):
    count = 0
    for i in range(1, len(p) - 1):
        if is_second_smallest(p, i):
            count += 1
    return count

def main():
    n, p = get_input()
    print(count_second_smallest(p))

if __name__ == '__main__':
    main()

