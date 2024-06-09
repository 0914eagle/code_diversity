
def f1(username):
    # count the number of distinct characters in the username
    num_distinct_chars = len(set(username))
    
    # if the number of distinct characters is odd, the user is male
    if num_distinct_chars % 2 == 1:
        return "IGNORE HIM!"
    # if the number of distinct characters is even, the user is female
    else:
        return "CHAT WITH HER!"

