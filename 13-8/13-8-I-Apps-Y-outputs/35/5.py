
def get_balanced_ternary_string(s):
    # Convert the input string to a list of characters
    char_list = list(s)
    
    # Initialize variables to keep track of the number of each character
    num_0s = char_list.count("0")
    num_1s = char_list.count("1")
    num_2s = char_list.count("2")
    
    # Initialize a dictionary to keep track of the minimum number of replacements needed for each character
    min_replacements = {"0": 0, "1": 0, "2": 0}
    
    # Loop through the characters of the string
    for i in range(len(s)):
        # If the current character is not the same as the character at the same index in the sorted string, we need to make a replacement
        if s[i] != sorted(s)[i]:
            # If the current character is "0", we can replace it with either "1" or "2"
            if s[i] == "0":
                min_replacements["0"] += 1
                min_replacements["1"] += 1
                min_replacements["2"] += 1
            # If the current character is "1", we can replace it with "2"
            elif s[i] == "1":
                min_replacements["1"] += 1
                min_replacements["2"] += 1
            # If the current character is "2", we can replace it with "0"
            else:
                min_replacements["2"] += 1
                min_replacements["0"] += 1
    
    # Initialize a list to store the characters of the balanced ternary string
    balanced_ternary_string = []
    
    # Loop through the characters of the input string
    for i in range(len(s)):
        # If the current character is not the same as the character at the same index in the sorted string, we need to make a replacement
        if s[i] != sorted(s)[i]:
            # If the current character is "0", we can replace it with either "1" or "2"
            if s[i] == "0":
                # If the number of replacements for "0" is the minimum, replace it with "1"
                if min_replacements["0"] == min(min_replacements.values()):
                    balanced_ternary_string.append("1")
                # Otherwise, replace it with "2"
                else:
                    balanced_ternary_string.append("2")
            # If the current character is "1", we can replace it with "2"
            elif s[i] == "1":
                # If the number of replacements for "1" is the minimum, replace it with "2"
                if min_replacements["1"] == min(min_replacements.values()):
                    balanced_ternary_string.append("2")
                # Otherwise, replace it with "0"
                else:
                    balanced_ternary_string.append("0")
            # If the current character is "2", we can replace it with "0"
            else:
                # If the number of replacements for "2" is the minimum, replace it with "0"
                if min_replacements["2"] == min(min_replacements.values()):
                    balanced_ternary_string.append("0")
                # Otherwise, replace it with "1"
                else:
                    balanced_ternary_string.append("1")
        # If the current character is the same as the character at the same index in the sorted string, we do not need to make a replacement
        else:
            balanced_ternary_string.append(s[i])
    
    return "".join(balanced_ternary_string)

