
def get_average_price(prices):
    return sum(prices) / len(prices)

def get_consecutive_sequences(prices, p):
    consecutive_sequences = 0
    for i in range(len(prices)):
        sequence_average = get_average_price(prices[i:])
        if sequence_average >= p:
            consecutive_sequences += 1
    return consecutive_sequences

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    p = int(input())
    print(get_consecutive_sequences(prices, p))

if __name__ == '__main__':
    main()

