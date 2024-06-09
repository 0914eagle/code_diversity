
def check_doublets(rolls):
    for i in range(len(rolls) - 2):
        if rolls[i] == rolls[i+1] == rolls[i+2]:
            return "Yes"
    return "No"

