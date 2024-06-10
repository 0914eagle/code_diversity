
def is_subsequence_sum_divisible(numbers, m):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if sum(numbers[i:j+1]) % m == 0:
                return True
    return False

def main():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    if is_subsequence_sum_divisible(numbers, m):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

