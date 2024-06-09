
def is_subsequence_divisible(numbers, m):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sum(numbers[i:j+1]) % m == 0:
                return "YES"
    return "NO"

def main():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(is_subsequence_divisible(numbers, m))

if __name__ == '__main__':
    main()

