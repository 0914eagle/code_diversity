
def get_min_operations(cards):
    # Initialize variables
    min_operations = 0
    prime_numbers = []
    consecutive_cards = []

    # Iterate through the cards and find all prime numbers
    for card in cards:
        if is_prime(card):
            prime_numbers.append(card)

    # Sort the prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Iterate through the prime numbers and find the minimum number of operations required to flip all the cards
    for prime in prime_numbers:
        # Find the consecutive cards that can be flipped with the current prime number
        consecutive_cards = get_consecutive_cards(cards, prime)

        # If all the cards are flipped, return the minimum number of operations required
        if len(consecutive_cards) == len(cards):
            return min_operations

        # Otherwise, increment the minimum number of operations required and continue
        min_operations += 1

    # If all the cards cannot be flipped, return -1
    return -1

def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Check if the number is divisible by 2 to n-1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    # If the number is less than or equal to 1, it is not prime
    return False

def get_consecutive_cards(cards, prime):
    consecutive_cards = []
    for i in range(len(cards)):
        if cards[i] % prime == 0:
            consecutive_cards.append(cards[i])
    return consecutive_cards

if __name__ == '__main__':
    num_cards = int(input())
    cards = list(map(int, input().split()))
    print(get_min_operations(cards))

