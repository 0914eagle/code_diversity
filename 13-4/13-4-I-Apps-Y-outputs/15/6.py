
def get_common_divisors(arr):
    divisors = set()
    for num in arr:
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.add(i)
    return len(divisors)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_common_divisors(arr))

if __name__ == '__main__':
    main()

