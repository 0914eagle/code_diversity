
def num_ways(encrypted_password):
    # Initialize a counter for the number of ways the password might have looked
    num_ways = 0
    
    # Iterate through each possible position in the password
    for i in range(len(encrypted_password)):
        # If the current position is a consonant, check if it was transformed correctly
        if encrypted_password[i].isalpha() and encrypted_password[i] != "a" and encrypted_password[i] != "e" and encrypted_password[i] != "i" and encrypted_password[i] != "o" and encrypted_password[i] != "u":
            # If the current position is not a vowel, check if the next position is a vowel
            if i < len(encrypted_password) - 1 and encrypted_password[i+1].isalpha() and encrypted_password[i+1] == "o":
                # If the next position is a vowel, increment the counter
                num_ways += 1
    
    # Return the number of ways the password might have looked
    return num_ways % 1000009

