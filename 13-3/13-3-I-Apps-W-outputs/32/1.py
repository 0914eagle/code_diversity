
def get_years_to_become_larger(a, b):
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    return years

