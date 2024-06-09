
def extended_name(y, p):
    if y.endswith("e"):
        return y + "x" + p
    elif y[-1] in "aiou":
        return y[:-1] + "ex" + p
    else:
        return y + "ex" + p

