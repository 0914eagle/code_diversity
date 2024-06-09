
def find_beautiful_number(p, x):
    # Initialize a list to store the possible numbers
    numbers = []
    
    # Iterate from 1 to 10^6
    for i in range(1, 1000001):
        # Check if the number has the required length
        if len(str(i)) == p:
            # Check if the number is strictly positive
            if i > 0:
                # Check if the number doesn't contain any leading zeroes
                if str(i) != "0" * p:
                    # Check if the number grows exactly x times when the last digit is moved to the beginning
                    if i * x == int(str(i)[1:] + str(i)[0]):
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

