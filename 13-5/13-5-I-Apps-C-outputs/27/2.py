
def f1(N):
    # Convert the binary string to an integer
    N = int(N, 2)
    
    # Initialize the number of representations to 0
    representations = 0
    
    # Iterate through all possible values of the leftmost bit
    for i in range(3):
        # Set the leftmost bit to the current value
        N_new = N | (i << (len(N) - 1))
        
        # If the new number is not equal to the original number, increment the number of representations
        if N_new != N:
            representations += 1
    
    # Return the number of representations modulo 1000000009
    return representations % 1000000009

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    N = input()
    print(f1(N))

