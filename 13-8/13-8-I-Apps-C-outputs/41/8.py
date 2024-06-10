
def riffle_shuffle(n, order):
    # Initialize the number of shuffles to 0
    shuffles = 0
    
    # Split the deck into two stacks
    stack1 = order[:n//2]
    stack2 = order[n//2:]
    
    # Interleave the stacks in a random order
    while stack1 and stack2:
        if random.random() < 0.5:
            order.append(stack1.pop())
        else:
            order.append(stack2.pop())
        shuffles += 1
    
    # If either stack is not empty, add the remaining cards to the end of the order
    while stack1:
        order.append(stack1.pop())
        shuffles += 1
    while stack2:
        order.append(stack2.pop())
        shuffles += 1
    
    return shuffles

def main():
    n = int(input())
    order = list(map(int, input().split()))
    print(riffle_shuffle(n, order))

if __name__ == '__main__':
    main()

