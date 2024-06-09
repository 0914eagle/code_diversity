
def get_min_ones(n):
    # Initialize a list to store the addends
    addends = []
    # Initialize a variable to store the current addend
    current_addend = 1
    # Iterate until the number is greater than 1
    while n > 1:
        # If the current addend is a factor of the number, add it to the list and divide the number by the addend
        if n % current_addend == 0:
            addends.append(current_addend)
            n //= current_addend
        # Otherwise, increment the current addend by 1
        else:
            current_addend += 1
    # Return the sum of the addends
    return sum(addends)

def main():
    n = int(input())
    print(get_min_ones(n))

if __name__ == '__main__':
    main()

