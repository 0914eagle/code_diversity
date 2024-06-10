
def get_bridges(a, b, c):
    # Initialize the number of bridges to 0
    num_bridges = 0
    
    # Loop through all possible combinations of bridges
    for i in range(1 << a):
        for j in range(1 << b):
            for k in range(1 << c):
                # Check if the current combination of bridges violates the restrictions
                if (i & j) and (j & k) and (i & k):
                    continue
                
                # Increment the number of bridges if the current combination is valid
                num_bridges += 1
    
    # Return the number of bridges modulo 998244353
    return num_bridges % 998244353

def main():
    a, b, c = map(int, input().split())
    print(get_bridges(a, b, c))

if __name__ == '__main__':
    main()

