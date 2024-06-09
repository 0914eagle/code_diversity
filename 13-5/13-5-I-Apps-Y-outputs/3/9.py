
def solve(ticket):
    for op1 in ["+", "-"]:
        for op2 in ["+", "-"]:
            for op3 in ["+", "-"]:
                if eval(ticket[0] + op1 + ticket[1] + op2 + ticket[2] + op3 + ticket[3]) == 7:
                    return ticket[0] + op1 + ticket[1] + op2 + ticket[2] + op3 + ticket[3] + "=" + "7"

