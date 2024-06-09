
def f1(user_name):
    # count the number of distinct characters in the user name
    num_distinct_chars = len(set(user_name))
    
    # if the number of distinct characters is odd, the user is male
    if num_distinct_chars % 2 == 1:
        return "IGNORE HIM!"
    # otherwise, the user is female
    else:
        return "CHAT WITH HER!"

