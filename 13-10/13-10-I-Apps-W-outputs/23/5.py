
def find_maximum_candies(n, k, M, D):
    maximum = 0
    for x in range(1, M + 1):
        if n % x == 0:
            count = 0
            for i in range(k):
                count += n // x
                if count > D:
                    break
            if count <= D:
                maximum = max(maximum, n // x)
    return maximum

def main():
    n, k, M, D = map(int, input().split())
    print(find_maximum_candies(n, k, M, D))

if __name__ == '__main__':
    main()

