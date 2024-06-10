
def count_bridges(a, b, c):
    # Initialize the number of bridges to 0
    num_bridges = 0
    
    # Loop over all possible pairs of islands
    for i in range(a):
        for j in range(i+1, a+b):
            # If the distance between the islands is at least 3, add a bridge
            if j - i >= 3:
                num_bridges += 1
    
    # Loop over all possible pairs of islands
    for i in range(a+b):
        for j in range(i+1, a+b+c):
            # If the distance between the islands is at least 3, add a bridge
            if j - i >= 3:
                num_bridges += 1
    
    # Return the number of bridges modulo 998244353
    return num_bridges % 998244353

def main():
    # Read the input
    a, b, c = map(int, input().split())
    
    # Call the count_bridges function and print the result
    print(count_bridges(a, b, c))

if __name__ == '__main__':
    main()

