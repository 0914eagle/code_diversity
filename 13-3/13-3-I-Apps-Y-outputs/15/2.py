
def get_available_megabytes(x, n, months_used):
    available_megabytes = x
    for month in months_used:
        available_megabytes -= month
        if available_megabytes < 0:
            available_megabytes = 0
    return available_megabytes

