
def check_string(a_00, a_01, a_10, a_11):
    # Initialize variables
    s = ""
    count = 0
    i = 0
    j = 0
    
    # Loop through the string
    while count < 1000000:
        # Add a character to the string
        if i == 0 and j == 0:
            s += "0"
            i += 1
        elif i == 1 and j == 0:
            s += "1"
            j += 1
        elif i == 0 and j == 1:
            s += "1"
            i += 1
        elif i == 1 and j == 1:
            s += "0"
            j += 1
        
        # Check if the string matches the given integers
        if s[0] == "0" and s[1] == "0":
            count += a_00
        if s[0] == "0" and s[1] == "1":
            count += a_01
        if s[0] == "1" and s[1] == "0":
            count += a_10
        if s[0] == "1" and s[1] == "1":
            count += a_11
        
        # If the string matches, return it
        if count == a_00 + a_01 + a_10 + a_11:
            return s
        
        # If the string doesn't match, continue the loop
        count = 0
        s = ""
        i = 0
        j = 0
    
    # If no string matches, return "Impossible"
    return "Impossible"

def main():
    # Read input
    a_00, a_01, a_10, a_11 = map(int, input().split())
    
    # Call the check_string function and print the result
    print(check_string(a_00, a_01, a_10, a_11))

if __name__ == '__main__':
    main()

