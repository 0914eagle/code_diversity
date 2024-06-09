
def is_haiku(phrases):
    A, B, C = phrases
    return A + B + C == 15 and A % 5 == 0 and B % 7 == 0 and C % 5 == 0

