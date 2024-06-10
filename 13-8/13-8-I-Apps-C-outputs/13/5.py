
def get_closest_handsome_numbers(n):
    # Convert the input number to a string
    n_str = str(n)
    
    # Initialize the closest handsome numbers as the input number itself
    closest_handsome_numbers = [n_str]
    
    # Iterate through the digits of the input number
    for i in range(len(n_str) - 1):
        # Check if the current digit and the next digit have the same parity
        if int(n_str[i]) % 2 == int(n_str[i+1]) % 2:
            # If they have the same parity, replace the current digit with the next digit
            closest_handsome_numbers[0] = closest_handsome_numbers[0][:i] + n_str[i+1] + closest_handsome_numbers[0][i+1:]
    
    # If the input number is handsome, return it as the only handsome number
    if is_handsome_number(n_str):
        return closest_handsome_numbers[0]
    
    # If the input number is not handsome, return the closest handsome numbers
    return " ".join(closest_handsome_numbers)

def is_handsome_number(n_str):
    # Check if the input number has only one digit
    if len(n_str) == 1:
        return True
    
    # Check if the input number has consecutive digits of different parity
    for i in range(len(n_str) - 1):
        if int(n_str[i]) % 2 == int(n_str[i+1]) % 2:
            return False
    
    return True

if __name__ == '__main__':
    n = int(input())
    print(get_closest_handsome_numbers(n))

