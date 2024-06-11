def file_name_check(file_name):
    
    # Your code here
    if file_name.count('.') != 1:
        return 'No'
    else:
        file_name_split = file_name.split('.')
        if len(file_name_split[0]) == 0:
            return 'No'
        elif file_name_split[0][0].isalpha() == False:
            return 'No'
        elif file_name_split[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        elif file_name_split[0].count('0') + file_name_split[0].count('1') + file_name_split[0].count('2') + file_name_split[0].count('3') + file_name_split[0].count('4') + file_name_split[0].count('5') + file_name_split[0].count('6') + file_name_split[0].count('7') + file_name_split[0].count('8') + file_name_split[0].count('9') > 3:
            return 'No'
        else:
            return 'Yes'


# +
# Test your code here
# -

# ### Exercise 2
#
# Write a function which takes a string representing a file's name, and returns the file's extension.
#
# Examples:
#
# file_extension("example.txt") # => 'txt'
#
# file_extension("example.new.txt") # => 'txt'
#
# file_extension("index") # => ''

