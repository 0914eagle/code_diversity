
def get_points(X):
    # Find the smallest number of factors needed to reach X
    num_factors = 1
    while X > 1:
        X //= 2
        num_factors += 1
    
    # Return the number of points obtained by the second player
    return num_factors

def main():
    X = int(input())
    print(get_points(X))

if __name__ == '__main__':
    main()

