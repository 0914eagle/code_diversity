
def solve(n):
    # find the quasibinary representation of n
    quasibinary_rep = ""
    while n > 0:
        quasibinary_rep = str(n % 2) + quasibinary_rep
        n //= 2
    
    # count the number of quasibinary numbers needed to represent n
    count = 0
    while len(quasibinary_rep) > 0:
        count += 1
        quasibinary_rep = quasibinary_rep.lstrip("0")
    
    # return the result
    return count, quasibinary_rep

