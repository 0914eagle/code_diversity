
def is_subsequence_divisible(numbers, m):
    # Iterate through the numbers and check if the sum of any subsequence is divisible by m
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sum(numbers[i:j+1]) % m == 0:
                return True
    return False

def main():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    if is_subsequence_divisible(numbers, m):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

