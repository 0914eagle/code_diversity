
def evaluate_formula(formula):
    # Split the formula into two parts: A and B
    A, op, B = formula.split()
    
    # Convert A and B to integers
    A = int(A)
    B = int(B)
    
    # Evaluate the formula using the operator
    if op == "+":
        result = A + B
    elif op == "-":
        result = A - B
    else:
        raise ValueError("Invalid operator")
    
    return result

def main():
    # Read a line of input from stdin and split it into A and B
    A, op, B = input().split()
    
    # Convert A and B to integers
    A = int(A)
    B = int(B)
    
    # Call the evaluate_formula function and print the result
    result = evaluate_formula(A, op, B)
    print(result)

if __name__ == '__main__':
    main()

