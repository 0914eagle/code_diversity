
def get_input():
    N = int(input())
    numbers = list(map(int, input().split()))
    return N, numbers

def f1(N, numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the numbers that are adjacent to the current number
    adjacent_numbers = []
    # Initialize a counter to keep track of the number of moves
    moves = 0
    # Initialize a boolean to keep track of whether Ivana has won
    has_won = False

    # Loop through each number in the input
    for number in numbers:
        # If the number has not been taken, add it to the taken numbers set
        if number not in taken_numbers:
            taken_numbers.add(number)
            # Add the number to the adjacent numbers list
            adjacent_numbers.append(number)
            # Increment the move counter
            moves += 1
            # If the number is odd, Ivana has won
            if number % 2 == 1:
                has_won = True
                break
        # If the number has been taken, find the adjacent numbers that have not been taken and add them to the list
        else:
            for adjacent_number in numbers:
                if adjacent_number not in taken_numbers and adjacent_number in get_adjacent_numbers(number, numbers):
                    adjacent_numbers.append(adjacent_number)
                    taken_numbers.add(adjacent_number)
                    moves += 1
                    if adjacent_number % 2 == 1:
                        has_won = True
                        break
        # If Ivana has won, break out of the loop
        if has_won:
            break

    # Return the number of moves Ivana can make
    return moves

def get_adjacent_numbers(number, numbers):
    # Find the index of the number in the list
    index = numbers.index(number)
    # Find the indices of the adjacent numbers
    left_index = index - 1 if index > 0 else len(numbers) - 1
    right_index = index + 1 if index < len(numbers) - 1 else 0
    # Return the adjacent numbers
    return [numbers[left_index], numbers[right_index]]

def f2(N, numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the numbers that are adjacent to the current number
    adjacent_numbers = []
    # Initialize a counter to keep track of the number of moves
    moves = 0
    # Initialize a boolean to keep track of whether Ivana has won
    has_won = False

    # Loop through each number in the input
    for number in numbers:
        # If the number has not been taken, add it to the taken numbers set
        if number not in taken_numbers:
            taken_numbers.add(number)
            # Add the number to the adjacent numbers list
            adjacent_numbers.append(number)
            # Increment the move counter
            moves += 1
            # If the number is odd, Ivana has won
            if number % 2 == 1:
                has_won = True
                break
        # If the number has been taken, find the adjacent numbers that have not been taken and add them to the list
        else:
            for adjacent_number in numbers:
                if adjacent_number not in taken_numbers and adjacent_number in get_adjacent_numbers(number, numbers):
                    adjacent_numbers.append(adjacent_number)
                    taken_numbers.add(adjacent_number)
                    moves += 1
                    if adjacent_number % 2 == 1:
                        has_won = True
                        break
        # If Ivana has won, break out of the loop
        if has_won:
            break

    # Return the number of moves Ivana can make
    return moves

if __name__ == '__main__':
    N, numbers = get_input()
    print(f1(N, numbers))
    print(f2(N, numbers))

