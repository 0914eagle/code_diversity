
def f1(user_name):
    # Count the number of distinct characters in the user name
    num_distinct_chars = len(set(user_name))
    
    # If the number of distinct characters is odd, the user is male
    if num_distinct_chars % 2 == 1:
        return "IGNORE HIM!"
    # Otherwise, the user is female
    else:
        return "CHAT WITH HER!"

