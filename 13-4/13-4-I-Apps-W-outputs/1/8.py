
def is_good_string(strings, s):
    # Check if all strings are substrings of s
    for string in strings:
        if string not in s:
            return False
    return True

def get_good_string(strings):
    # Initialize the minimum length and the good string
    min_len = float('inf')
    good_string = ""

    # Iterate over all possible substrings
    for i in range(len(strings[0])):
        for j in range(i+1, len(strings[0])+1):
            # Check if the substring is good
            substring = strings[0][i:j]
            if is_good_string(strings, substring):
                # If it is good, check if it is the minimum length
                if len(substring) < min_len:
                    min_len = len(substring)
                    good_string = substring

    # If no good string is found, return "NO"
    if good_string == "":
        return "NO"

    # Otherwise, return the good string
    return good_string

