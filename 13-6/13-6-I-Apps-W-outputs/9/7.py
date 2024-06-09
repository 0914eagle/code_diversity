
def get_lucky_index(n):
    lucky_digits = ["4", "7"]
    n_str = str(n)
    count = 0
    for i in range(len(n_str)):
        if n_str[i] in lucky_digits:
            count += 1
    return count

