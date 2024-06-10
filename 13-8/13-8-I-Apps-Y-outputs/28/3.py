
def find_equation(numbers):
    # Convert the input string to a list of integers
    numbers = [int(x) for x in numbers.split()]
    
    # Find the two numbers that add up to the third number
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == numbers[2]:
                return str(numbers[0]) + "+" + str(numbers[1]) + "=" + str(numbers[2])
    
    # If no solution is found, return "Impossible"
    return "Impossible"

def main():
    numbers = input("Enter three integers: ")
    print(find_equation(numbers))

if __name__ == '__main__':
    main()

