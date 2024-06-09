
def solve(score):
    if score == 0:
        return "zero"
    elif score == 1:
        return "one"
    elif score == 2:
        return "two"
    elif score == 3:
        return "three"
    elif score == 4:
        return "four"
    elif score == 5:
        return "five"
    elif score == 6:
        return "six"
    elif score == 7:
        return "seven"
    elif score == 8:
        return "eight"
    elif score == 9:
        return "nine"
    elif score == 10:
        return "ten"
    elif score == 11:
        return "eleven"
    elif score == 12:
        return "twelve"
    elif score == 13:
        return "thirteen"
    elif score == 14:
        return "fourteen"
    elif score == 15:
        return "fifteen"
    elif score == 16:
        return "sixteen"
    elif score == 17:
        return "seventeen"
    elif score == 18:
        return "eighteen"
    elif score == 19:
        return "nineteen"
    elif score == 20:
        return "twenty"
    elif score == 30:
        return "thirty"
    elif score == 40:
        return "forty"
    elif score == 50:
        return "fifty"
    elif score == 60:
        return "sixty"
    elif score == 70:
        return "seventy"
    elif score == 80:
        return "eighty"
    elif score == 90:
        return "ninety"
    elif score == 100:
        return "hundred"
    else:
        if score % 10 == 0:
            return solve(score - score % 10)
        else:
            return solve(score - score % 10) + "-" + solve(score % 10)

