
def get_number_of_moves(numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the moves
    moves = []
    # Iterate through the numbers
    for number in numbers:
        # If the number has not been taken, add it to the set of taken numbers and add the move to the list
        if number not in taken_numbers:
            taken_numbers.add(number)
            moves.append(number)
        # If the number has been taken, find the two adjacent numbers that have not been taken and add them to the set of taken numbers and the list of moves
        else:
            for i in range(1, len(numbers)):
                if (number + i) % len(numbers) not in taken_numbers and (number - i) % len(numbers) not in taken_numbers:
                    taken_numbers.add((number + i) % len(numbers))
                    taken_numbers.add((number - i) % len(numbers))
                    moves.append((number + i) % len(numbers))
                    moves.append((number - i) % len(numbers))
                    break
    # Return the length of the list of moves
    return len(moves)

def main():
    # Read the input
    n = int(input())
    numbers = [int(i) for i in input().split()]
    # Call the function to get the number of moves
    result = get_number_of_moves(numbers)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

