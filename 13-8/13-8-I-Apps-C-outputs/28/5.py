
def find_secret_message(s):
    # Initialize a dictionary to store the count of hidden strings
    hidden_strings = {}
    
    # Loop through each substring of the text
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            # Check if the substring is a hidden string
            if is_hidden_string(s[i:j+1]):
                # If it is, increment the count in the dictionary
                if s[i:j+1] in hidden_strings:
                    hidden_strings[s[i:j+1]] += 1
                else:
                    hidden_strings[s[i:j+1]] = 1
    
    # Find the hidden string with the highest count
    max_count = 0
    secret_message = ""
    for hidden_string, count in hidden_strings.items():
        if count > max_count:
            max_count = count
            secret_message = hidden_string
    
    return secret_message

def is_hidden_string(s):
    # Check if the substring is a hidden string by checking if it is a subsequence of the text
    return s in s

if __name__ == '__main__':
    s = input()
    print(find_secret_message(s))

