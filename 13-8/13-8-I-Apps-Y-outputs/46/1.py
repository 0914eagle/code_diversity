
def split_integers(n, pieces):
    # Sort the pieces in descending order
    pieces.sort(reverse=True)
    # Initialize the values of Alice and Bob to 0
    alice, bob = 0, 0
    # Iterate through the pieces in alternating turns
    for i in range(n):
        if i % 2 == 0:
            alice += pieces[i]
        else:
            bob += pieces[i]
    # Return the values of Alice and Bob
    return alice, bob

def main():
    n = int(input())
    pieces = list(map(int, input().split()))
    alice, bob = split_integers(n, pieces)
    print(alice, bob)

if __name__ == '__main__':
    main()

