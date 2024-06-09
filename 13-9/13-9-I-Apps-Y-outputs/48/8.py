
def is_haiku(phrase_lengths):
    A, B, C = phrase_lengths
    return A + B + C == 15 and B - A == 2 and C - B == 2

