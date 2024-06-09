
def get_time_to_ahead(a, b, w, x, c):
    if c <= a:
        return 0
    if b >= x:
        b -= x
    else:
        a -= 1
        b = w - (x - b)
    return 1 + get_time_to_ahead(a, b, w, x, c-1)

