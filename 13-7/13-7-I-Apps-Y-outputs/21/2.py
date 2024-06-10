
def get_min_snacks(guests_a, guests_b):
    # Find the smaller number of guests
    if guests_a < guests_b:
        smaller_guests = guests_a
    else:
        smaller_guests = guests_b
    
    # Find the larger number of guests
    if guests_a > guests_b:
        larger_guests = guests_a
    else:
        larger_guests = guests_b
    
    # Calculate the minimum number of snacks needed for the smaller number of guests
    min_snacks = smaller_guests
    
    # Calculate the minimum number of snacks needed for the larger number of guests
    while min_snacks < larger_guests:
        min_snacks += smaller_guests
    
    return min_snacks

def main():
    guests_a, guests_b = map(int, input().split())
    print(get_min_snacks(guests_a, guests_b))

if __name__ == '__main__':
    main()

