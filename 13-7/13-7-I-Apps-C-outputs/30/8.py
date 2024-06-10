
def get_subsequences(prices, p):
    subsequences = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)+1):
            if sum(prices[i:j])/j >= p:
                subsequences.append(prices[i:j])
    return len(set(map(tuple, subsequences)))

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    p = int(input())
    print(get_subsequences(prices, p))

if __name__ == '__main__':
    main()

