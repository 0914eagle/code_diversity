
def round_to_nearest(candy_price, k):
    # Find the nearest power of 10 that is greater than or equal to the candy price
    nearest_power = 10**k
    while nearest_power < candy_price:
        nearest_power *= 10
    
    # Round the candy price to the nearest power of 10
    return nearest_power

def main():
    candy_price, k = map(int, input().split())
    print(round_to_nearest(candy_price, k))

if __name__ == '__main__':
    main()

