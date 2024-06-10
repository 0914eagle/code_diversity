
def get_average_price(prices):
    return sum(prices) / len(prices)

def get_consecutive_sequences(prices, p):
    sequences = []
    for i in range(len(prices)):
        sequence = [prices[i]]
        for j in range(i+1, len(prices)):
            if get_average_price(sequence) >= p:
                sequences.append(sequence)
                break
            sequence.append(prices[j])
    return sequences

def count_consecutive_sequences(prices, p):
    sequences = get_consecutive_sequences(prices, p)
    return len(sequences)

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    p = int(input())
    print(count_consecutive_sequences(prices, p))

if __name__ == '__main__':
    main()

