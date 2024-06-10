
def shuffle(n, cards):
    # Initialize the number of shuffles to 0
    shuffles = 0
    
    # Split the deck into two stacks
    stack1 = cards[:n//2]
    stack2 = cards[n//2:]
    
    # Interleave the stacks in a random order
    while stack1 and stack2:
        shuffles += 1
        if len(stack1) > len(stack2):
            stack1.append(stack1.pop(0))
        else:
            stack2.append(stack2.pop(0))
    
    # Return the number of shuffles
    return shuffles

def main():
    # Read the input
    n = int(input())
    cards = list(map(int, input().split()))
    
    # Determine the minimum number of shuffles
    shuffles = shuffle(n, cards)
    
    # Print the output
    print(shuffles)

if __name__ == '__main__':
    main()

