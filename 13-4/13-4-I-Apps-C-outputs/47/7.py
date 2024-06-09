
def get_closest_handsome_numbers(n):
    # Convert the input number to a list of individual digits
    digits = [int(d) for d in str(n)]
    
    # Initialize variables to keep track of the closest handsome numbers
    closest_handsome_numbers = []
    closest_distance = float('inf')
    
    # Iterate through all possible handsome numbers
    for i in range(10**(len(digits)-1)):
        # Convert the current handsome number to a list of individual digits
        handsome_digits = [int(d) for d in str(i)]
        
        # Check if the current handsome number is closer to the input number than the previous closest handsome number
        distance = abs(n - i)
        if distance < closest_distance:
            closest_distance = distance
            closest_handsome_numbers = [i]
        elif distance == closest_distance:
            closest_handsome_numbers.append(i)
    
    # Return the closest handsome numbers
    return closest_handsome_numbers

def main():
    n = int(input())
    handsome_numbers = get_closest_handsome_numbers(n)
    print(*handsome_numbers)

if __name__ == '__main__':
    main()

