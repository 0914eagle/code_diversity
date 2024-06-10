
def get_number_of_bridges(a, b, c):
    # Initialize the number of bridges to 0
    num_bridges = 0
    
    # Loop over all possible combinations of bridges between red and blue islands
    for i in range(a):
        for j in range(b):
            # Check if the distance between the two islands is at least 3
            if i + j >= 3:
                # Increment the number of bridges
                num_bridges += 1
    
    # Loop over all possible combinations of bridges between red and purple islands
    for i in range(a):
        for j in range(c):
            # Check if the distance between the two islands is at least 3
            if i + j >= 3:
                # Increment the number of bridges
                num_bridges += 1
    
    # Loop over all possible combinations of bridges between blue and purple islands
    for i in range(b):
        for j in range(c):
            # Check if the distance between the two islands is at least 3
            if i + j >= 3:
                # Increment the number of bridges
                num_bridges += 1
    
    # Return the number of bridges modulo 998 244 353
    return num_bridges % 998244353

def main():
    # Read the input a, b, and c
    a, b, c = map(int, input().split())
    
    # Call the get_number_of_bridges function and print the result
    print(get_number_of_bridges(a, b, c))

if __name__ == '__main__':
    main()

