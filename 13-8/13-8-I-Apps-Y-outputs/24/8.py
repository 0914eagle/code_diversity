
def is_easily_playable(s):
    # Initialize variables to keep track of the number of R, U, and D characters
    num_r = 0
    num_u = 0
    num_d = 0
    
    # Iterate through the string and check if the characters are R, U, or D
    for i, char in enumerate(s):
        if char == "R":
            num_r += 1
        elif char == "U":
            num_u += 1
        elif char == "D":
            num_d += 1
    
    # Check if the number of R, U, and D characters are equal in both odd and even positions
    if num_r == num_u and num_r == num_d and num_r % 2 == 0:
        return "Yes"
    else:
        return "No"

def main():
    s = input()
    print(is_easily_playable(s))

if __name__ == "__main__":
    main()

