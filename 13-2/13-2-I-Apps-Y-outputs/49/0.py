
def is_balanced(s):
    # Initialize the number of black and white stones
    black_stones = 0
    white_stones = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # Check if the current stone is black or white
        if s[i] == "B":
            black_stones += 1
        else:
            white_stones += 1
        
        # Check if the difference between black and white stones is more than 1
        if abs(black_stones - white_stones) > 1:
            return False
    
    # If the difference is 0 or 1, return True
    return True

def main():
    s = input()
    print(is_balanced(s))

if __name__ == "__main__":
    main()

