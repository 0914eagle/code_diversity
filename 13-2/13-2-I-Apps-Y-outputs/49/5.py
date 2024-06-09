
def is_balanced(s):
    # Initialize the number of black and white stones
    black_stones = 0
    white_stones = 0
    
    # Iterate through the string
    for stone in s:
        if stone == "B":
            black_stones += 1
        else:
            white_stones += 1
    
    # Check if the number of black and white stones is equal
    return black_stones == white_stones

def main():
    s = input()
    print(is_balanced(s))

if __name__ == '__main__':
    main()

