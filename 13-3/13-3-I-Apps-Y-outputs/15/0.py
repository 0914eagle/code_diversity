
def get_available_megabytes(x, n, months_spent):
    available_megabytes = x
    for i in range(n):
        available_megabytes += months_spent[i]
        available_megabytes -= x
    return available_megabytes

