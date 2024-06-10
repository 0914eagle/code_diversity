
def get_average_price(prices):
    return sum(prices) / len(prices)

def get_consecutive_subsequences(prices, p):
    subsequences = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)+1):
            if get_average_price(prices[i:j]) >= p:
                subsequences.append(prices[i:j])
    return subsequences

def count_distinct_subsequences(subsequences):
    return len(set(map(tuple, subsequences)))

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    p = int(input())
    subsequences = get_consecutive_subsequences(prices, p)
    print(count_distinct_subsequences(subsequences))

if __name__ == '__main__':
    main()

