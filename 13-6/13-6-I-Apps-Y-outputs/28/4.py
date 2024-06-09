
def evaluate_formula(formula):
    A, op, B = formula.split()
    A = int(A)
    B = int(B)
    if op == "+":
        return A + B
    else:
        return A - B

def main():
    formula = input("Enter a formula (e.g. 1 + 2): ")
    result = evaluate_formula(formula)
    print(result)

if __name__ == '__main__':
    main()

