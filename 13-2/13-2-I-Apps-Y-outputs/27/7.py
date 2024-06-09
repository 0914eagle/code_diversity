
def count_second_smallest(p):
    n = len(p)
    count = 0
    for i in range(1, n-1):
        if p[i] < p[i-1] and p[i] < p[i+1]:
            count += 1
    return count

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(count_second_smallest(p))

if __name__ == '__main__':
    main()

