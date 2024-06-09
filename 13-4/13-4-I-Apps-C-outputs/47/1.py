
def is_handsome(num):
    # Check if the number has only one digit
    if len(str(num)) == 1:
        return True
    
    # Check if the number has consecutive digits of different parity
    prev_digit = str(num)[0]
    for digit in str(num)[1:]:
        if prev_digit == digit:
            return False
        prev_digit = digit
    return True

def find_closest_handsome(num):
    # Find the closest handsome number to the left
    left = num
    while not is_handsome(left):
        left -= 1
    
    # Find the closest handsome number to the right
    right = num
    while not is_handsome(right):
        right += 1
    
    # Return the smaller number and the larger number separated by a space
    return str(left) + " " + str(right)

if __name__ == '__main__':
    num = int(input())
    print(find_closest_handsome(num))

