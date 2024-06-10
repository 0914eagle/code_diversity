
def riffle_shuffle(deck, n):
    # Split the deck into two stacks
    stack1 = deck[:n//2]
    stack2 = deck[n//2:]
    
    # Interleave the two stacks
    interleaved = [stack1[0]]
    for i in range(1, n):
        if i % 2 == 0:
            interleaved.append(stack1[i])
        else:
            interleaved.append(stack2[i])
    
    return interleaved

def shuffle_count(deck, n):
    # Initialize the shuffle count to 0
    count = 0
    
    # While the deck is not in the correct order
    while deck != list(range(1, n+1)):
        # Shuffle the deck
        deck = riffle_shuffle(deck, n)
        count += 1
    
    # Return the shuffle count
    return count

if __name__ == '__main__':
    n = int(input())
    deck = list(map(int, input().split()))
    print(shuffle_count(deck, n))

