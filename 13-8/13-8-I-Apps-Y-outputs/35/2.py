
def get_balanced_ternary_string(s):
    # Convert the string to a list of characters
    s_list = list(s)
    
    # Count the number of each character in the string
    count_0 = s_list.count("0")
    count_1 = s_list.count("1")
    count_2 = s_list.count("2")
    
    # Find the character that appears the least number of times
    if count_0 <= count_1 and count_0 <= count_2:
        least_common = "0"
    elif count_1 <= count_0 and count_1 <= count_2:
        least_common = "1"
    else:
        least_common = "2"
    
    # Replace all occurrences of the least common character with the most common character
    most_common = "0" if least_common == "2" else "1" if least_common == "0" else "2"
    s_list = [most_common if x == least_common else x for x in s_list]
    
    # Return the string
    return "".join(s_list)

