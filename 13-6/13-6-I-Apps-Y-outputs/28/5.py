
def evaluate_formula(formula):
    A, op, B = formula.split()
    if op == "+":
        return int(A) + int(B)
    else:
        return int(A) - int(B)

def main():
    formula = input()
    print(evaluate_formula(formula))

if __name__ == '__main__':
    main()

