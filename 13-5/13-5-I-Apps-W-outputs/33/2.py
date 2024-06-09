
def solve(s):
    if s == 0:
        return "zero"
    elif s == 1:
        return "one"
    elif s == 2:
        return "two"
    elif s == 3:
        return "three"
    elif s == 4:
        return "four"
    elif s == 5:
        return "five"
    elif s == 6:
        return "six"
    elif s == 7:
        return "seven"
    elif s == 8:
        return "eight"
    elif s == 9:
        return "nine"
    elif s == 10:
        return "ten"
    elif s == 11:
        return "eleven"
    elif s == 12:
        return "twelve"
    elif s == 13:
        return "thirteen"
    elif s == 14:
        return "fourteen"
    elif s == 15:
        return "fifteen"
    elif s == 16:
        return "sixteen"
    elif s == 17:
        return "seventeen"
    elif s == 18:
        return "eighteen"
    elif s == 19:
        return "nineteen"
    elif s == 20:
        return "twenty"
    elif s == 30:
        return "thirty"
    elif s == 40:
        return "forty"
    elif s == 50:
        return "fifty"
    elif s == 60:
        return "sixty"
    elif s == 70:
        return "seventy"
    elif s == 80:
        return "eighty"
    elif s == 90:
        return "ninety"
    elif s == 100:
        return "hundred"
    else:
        if s % 10 == 0:
            return solve(s - s % 10)
        else:
            return solve(s - s % 10) + "-" + solve(s % 10)

