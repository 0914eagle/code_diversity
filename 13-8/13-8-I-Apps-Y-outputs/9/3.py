
def get_maximum_candies(n, k):
    candies_per_kid = n // k
    extra_candies = n % k
    if extra_candies == 0:
        return candies_per_kid
    else:
        return candies_per_kid + 1

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n, k = map(int, input().split())
        print(get_maximum_candies(n, k))

if __name__ == '__main__':
    main()

