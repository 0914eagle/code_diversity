
def count_bouquets(n, a, b):
    # Initialize a list to store the numbers of bouquets for each number of flowers
    num_bouquets = [0] * (n + 1)
    num_bouquets[0] = 1
    
    # Iterate over the numbers of flowers
    for num_flowers in range(1, n + 1):
        # If the number of flowers is not equal to a or b, add the number of bouquets for the previous number of flowers
        if num_flowers != a and num_flowers != b:
            num_bouquets[num_flowers] += num_bouquets[num_flowers - 1]
        # Add the number of bouquets for the current number of flowers
        num_bouquets[num_flowers] += num_bouquets[num_flowers - 1]
    
    # Return the number of bouquets modulo (10^9 + 7)
    return num_bouquets[n] % (10**9 + 7)

def main():
    n, a, b = map(int, input().split())
    print(count_bouquets(n, a, b))

if __name__ == '__main__':
    main()

