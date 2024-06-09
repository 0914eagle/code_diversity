
def get_min_breaks(k):
    # Find the smallest power of two greater than or equal to k
    n = 1
    while n < k:
        n *= 2
    
    # The smallest bar size Mirko must buy is n
    # The number of breaks is the difference between n and k
    return n, n - k

def get_min_bar_size(k):
    # Find the smallest power of two greater than or equal to k
    n = 1
    while n < k:
        n *= 2
    
    # Return the smallest bar size
    return n

def main():
    k = int(input())
    print(get_min_breaks(k))
    print(get_min_bar_size(k))

if __name__ == "__main__":
    main()

