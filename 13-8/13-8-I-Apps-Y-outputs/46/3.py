
def split_integer(n, pieces):
    # Sort the pieces in descending order
    pieces.sort(reverse=True)
    
    # Initialize the values of Alice and Bob to 0
    alice_value = 0
    bob_value = 0
    
    # Iterate through the pieces in alternating turns
    for i in range(n):
        if i % 2 == 0:
            alice_value += pieces[i]
        else:
            bob_value += pieces[i]
    
    # Return the combined values of Alice and Bob
    return alice_value, bob_value

def main():
    n = int(input())
    pieces = list(map(int, input().split()))
    alice_value, bob_value = split_integer(n, pieces)
    print(alice_value, bob_value)

if __name__ == '__main__':
    main()

