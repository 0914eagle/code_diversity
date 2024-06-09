
def find_beautiful_number(p, x):
    # Initialize a list to store the possible numbers
    numbers = []
    
    # Iterate from 1 to 10^6
    for i in range(1, 10**6):
        # Convert the number to a string
        num_str = str(i)
        
        # Check if the number has the required length
        if len(num_str) == p:
            # Check if the number has no leading zeroes
            if num_str.lstrip("0") == num_str:
                # Check if the number grows by x times when the last digit is moved to the beginning
                if int(num_str[-1]) * x == int(num_str[1:] + num_str[0]):
                    numbers.append(i)
    
    # Check if at least one number was found
    if len(numbers) > 0:
        # Return the minimum number
        return min(numbers)
    else:
        # Return "Impossible" if no number was found
        return "Impossible"

def main():
    p, x = map(int, input().split())
    print(find_beautiful_number(p, x))

if __name__ == '__main__':
    main()

