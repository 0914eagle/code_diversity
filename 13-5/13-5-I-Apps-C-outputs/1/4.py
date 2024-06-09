
def get_largest_base(y, ell):
    # Initialize the largest base found so far
    largest_base = 0
    # Iterate through the possible bases
    for base in range(2, 11):
        # Convert the age to the current base
        converted_age = int(str(y), base)
        # Check if the converted age contains only decimal digits
        if all(int(digit) < base for digit in str(converted_age)):
            # Check if the converted age is at least the lower bound
            if converted_age >= ell:
                # If it is, update the largest base found so far
                largest_base = base
                break
    return largest_base

def main():
    y, ell = map(int, input().split())
    print(get_largest_base(y, ell))

if __name__ == '__main__':
    main()

