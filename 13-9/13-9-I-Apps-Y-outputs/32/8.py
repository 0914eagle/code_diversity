
def count_new_stones(S):
    # Initialize variables
    black_count = 0
    white_count = 0
    new_stones_needed = 0

    # Loop through the string S
    for stone in S:
        if stone == "B":
            black_count += 1
        else:
            white_count += 1

    # Check if all stones are the same color
    if black_count == 0 or white_count == 0:
        return 0

    # Calculate the minimum number of new stones needed
    if black_count > white_count:
        new_stones_needed = black_count - white_count
    else:
        new_stones_needed = white_count - black_count

    return new_stones_needed

def main():
    S = input()
    print(count_new_stones(S))

if __name__ == '__main__':
    main()

