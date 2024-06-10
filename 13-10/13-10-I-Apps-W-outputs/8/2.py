
def get_divisible_by_90_number(cards):
    # Initialize a list to store the numbers
    numbers = []
    
    # Iterate through the cards and append the numbers to the list
    for card in cards:
        if card == 0:
            numbers.append(0)
        else:
            numbers.append(5)
    
    # Initialize a variable to store the maximum number divisible by 90
    max_number = -1
    
    # Iterate through the possible combinations of numbers
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                number = int("".join(map(str, numbers[i:j]))) * 10 + int("".join(map(str, numbers[j:k])))
                if number % 90 == 0 and number > max_number:
                    max_number = number
    
    return max_number

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    print(get_divisible_by_90_number(cards))

if __name__ == '__main__':
    main()

