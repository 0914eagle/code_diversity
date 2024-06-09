
def get_min_operations(cards):
    # Initialize variables
    min_operations = 0
    prime_numbers = []
    consecutive_cards = []

    # Iterate through the cards and find the prime numbers
    for card in cards:
        if is_prime(card):
            prime_numbers.append(card)

    # Sort the prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Iterate through the prime numbers and find the consecutive cards
    for prime in prime_numbers:
        consecutive_cards.append(prime)
        if len(consecutive_cards) == prime:
            min_operations += 1
            consecutive_cards = []

    return min_operations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    num_cards = int(input())
    cards = list(map(int, input().split()))
    print(get_min_operations(cards))

