
def shuffle(n, cards):
    # Initialize the number of shuffles to 0
    shuffles = 0
    
    # Split the deck into two stacks
    stack_1 = cards[:n//2]
    stack_2 = cards[n//2:]
    
    # Interleave the stacks in a random order
    interleaved = []
    while stack_1 and stack_2:
        interleaved.append(stack_1.pop())
        interleaved.append(stack_2.pop())
    
    # Add any remaining cards to the end of the list
    while stack_1:
        interleaved.append(stack_1.pop())
    while stack_2:
        interleaved.append(stack_2.pop())
    
    # Check if the deck is now in the desired order
    if interleaved == cards:
        return shuffles
    
    # If not, recurse on the interleaved deck
    return 1 + shuffle(n, interleaved)

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    print(shuffle(n, cards))

if __name__ == '__main__':
    main()

