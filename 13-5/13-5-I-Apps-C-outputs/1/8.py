
def get_largest_base(y, ell):
    # Initialize the largest base to be 10
    largest_base = 10
    
    # Iterate through the possible bases from 2 to 16
    for base in range(2, 17):
        # Convert the age to the current base
        converted_age = int(str(y), base)
        
        # Check if the converted age contains only decimal digits
        if all(int(i) >= 0 and int(i) <= 9 for i in str(converted_age)):
            # Check if the converted age is at least the lower bound
            if converted_age >= ell:
                # Update the largest base if necessary
                largest_base = max(largest_base, base)
    
    return largest_base

def main():
    y, ell = map(int, input().split())
    print(get_largest_base(y, ell))

if __name__ == '__main__':
    main()

