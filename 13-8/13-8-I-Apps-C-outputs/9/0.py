
def get_meow_factor(string):
    # Initialize a variable to keep track of the minimum number of operations needed
    min_operations = float('inf')
    
    # Loop through all possible positions of the word "meow" in the string
    for i in range(len(string) - 2):
        # Check if the substring starting at position i and ending at position i+2 is "meow"
        if string[i:i+3] == "meow":
            # If it is, return 0 since it takes 0 operations to transform the string into a string with "meow" as a substring
            return 0
        # If the substring is not "meow", loop through all possible operations that can be performed on the string
        for operation in ["insert", "delete", "replace", "swap"]:
            # If the operation is "insert", loop through all possible characters that can be inserted
            if operation == "insert":
                for j in range(len(string) + 1):
                    # Check if inserting a character at position j would result in the word "meow"
                    if string[:j] + "meow" + string[j:] == "meow":
                        # If it would, update the minimum number of operations needed
                        min_operations = min(min_operations, 1)
            # If the operation is "delete", loop through all possible characters that can be deleted
            elif operation == "delete":
                for j in range(len(string)):
                    # Check if deleting the character at position j would result in the word "meow"
                    if string[:j] + string[j+1:] == "meow":
                        # If it would, update the minimum number of operations needed
                        min_operations = min(min_operations, 1)
            # If the operation is "replace", loop through all possible characters that can be replaced
            elif operation == "replace":
                for j in range(len(string)):
                    # Check if replacing the character at position j would result in the word "meow"
                    if string[:j] + "meow" + string[j+1:] == "meow":
                        # If it would, update the minimum number of operations needed
                        min_operations = min(min_operations, 1)
            # If the operation is "swap", loop through all possible swaps
            elif operation == "swap":
                for j in range(len(string) - 1):
                    # Check if swapping the characters at positions j and j+1 would result in the word "meow"
                    if string[:j] + string[j+1] + string[j] + string[j+2:] == "meow":
                        # If it would, update the minimum number of operations needed
                        min_operations = min(min_operations, 1)
    
    # If no operation results in the word "meow", return the minimum number of operations needed
    return min_operations

def main():
    string = input("Enter a string: ")
    print(get_meow_factor(string))

if __name__ == '__main__':
    main()

