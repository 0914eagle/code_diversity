
def generate_string(S):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character in S
    for char in S:
        # If the character is a digit, append it to the result string
        if char.isdigit():
            result += char
        # If the character is a 2, append 22 to the result string
        elif char == "2":
            result += "22"
        # If the character is a 3, append 333 to the result string
        elif char == "3":
            result += "333"
        # If the character is a 4, append 4444 to the result string
        elif char == "4":
            result += "4444"
        # If the character is a 5, append 55555 to the result string
        elif char == "5":
            result += "55555"
        # If the character is a 6, append 666666 to the result string
        elif char == "6":
            result += "666666"
        # If the character is a 7, append 7777777 to the result string
        elif char == "7":
            result += "7777777"
        # If the character is a 8, append 88888888 to the result string
        elif char == "8":
            result += "88888888"
        # If the character is a 9, append 999999999 to the result string
        elif char == "9":
            result += "999999999"
    
    # Return the result string
    return result

def get_kth_character(S, K):
    # Generate the string after 5*10^15 days
    result = generate_string(S)
    
    # Return the K-th character from the left in the string
    return result[K-1]

if __name__ == '__main__':
    S = input()
    K = int(input())
    print(get_kth_character(S, K))

