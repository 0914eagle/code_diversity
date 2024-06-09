
def get_available_megabytes(x, n, months_spent):
    available_megabytes = x
    for i in range(n):
        available_megabytes -= months_spent[i]
        if available_megabytes < 0:
            available_megabytes = 0
    return available_megabytes

