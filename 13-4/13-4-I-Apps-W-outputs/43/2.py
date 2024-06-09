
def get_unique_promo_code(promo_codes):
    # Initialize a dictionary to store the count of each digit
    digit_count = {}
    for promo_code in promo_codes:
        for digit in promo_code:
            if digit not in digit_count:
                digit_count[digit] = 1
            else:
                digit_count[digit] += 1
    
    # Find the digit with the minimum count
    min_count = min(digit_count.values())
    
    # Return the number of errors that can be tolerated
    return len(promo_code) - min_count

def main():
    n = int(input())
    promo_codes = []
    for _ in range(n):
        promo_codes.append(input())
    print(get_unique_promo_code(promo_codes))

if __name__ == '__main__':
    main()

