
def solve(s):
    if s == 0:
        return "zero"
    if s == 1:
        return "one"
    if s == 2:
        return "two"
    if s == 3:
        return "three"
    if s == 4:
        return "four"
    if s == 5:
        return "five"
    if s == 6:
        return "six"
    if s == 7:
        return "seven"
    if s == 8:
        return "eight"
    if s == 9:
        return "nine"
    if s == 10:
        return "ten"
    if s == 11:
        return "eleven"
    if s == 12:
        return "twelve"
    if s == 13:
        return "thirteen"
    if s == 14:
        return "fourteen"
    if s == 15:
        return "fifteen"
    if s == 16:
        return "sixteen"
    if s == 17:
        return "seventeen"
    if s == 18:
        return "eighteen"
    if s == 19:
        return "nineteen"
    if s == 20:
        return "twenty"
    if s == 30:
        return "thirty"
    if s == 40:
        return "forty"
    if s == 50:
        return "fifty"
    if s == 60:
        return "sixty"
    if s == 70:
        return "seventy"
    if s == 80:
        return "eighty"
    if s == 90:
        return "ninety"
    if s == 100:
        return "hundred"
    if s > 100:
        if s % 100 == 0:
            return solve(s // 100) + "hundred"
        else:
            return solve(s // 100) + "hundredand" + solve(s % 100)

