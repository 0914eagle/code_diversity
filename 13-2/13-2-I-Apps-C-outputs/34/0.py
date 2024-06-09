
def interpret_basic(program):
    # Initialize the variables
    variables = {}
    for line in program:
        # Split the line into label and statement
        label, statement = line.split()
        # Check if the statement is a LET statement
        if statement.startswith("LET"):
            # Extract the variable name and value
            var_name, var_value = statement.split("=")
            # Evaluate the value and store it in the variables dictionary
            variables[var_name] = eval_expression(var_value, variables)
        # Check if the statement is a PRINT or PRINTLN statement
        elif statement.startswith("PRINT"):
            # Extract the print statement
            print_statement = statement.split("PRINT")[1]
            # Evaluate the print statement and print the result
            print(eval_expression(print_statement, variables), end="")
        elif statement.startswith("PRINTLN"):
            # Extract the print statement
            print_statement = statement.split("PRINTLN")[1]
            # Evaluate the print statement and print the result with a newline
            print(eval_expression(print_statement, variables))
    # Return the variables dictionary
    return variables

def eval_expression(expression, variables):
    # Check if the expression is a variable
    if expression.isalpha():
        return variables[expression]
    # Check if the expression is an arithmetic operation
    if "+" in expression or "-" in expression or "*" in expression or "/" in expression:
        # Extract the operands and the operator
        operands = expression.split()
        operator = operands[1]
        # Evaluate the operands recursively
        op1 = eval_expression(operands[0], variables)
        op2 = eval_expression(operands[2], variables)
        # Perform the arithmetic operation
        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            return op1 // op2
    # Check if the expression is a comparison
    if "=" in expression or ">" in expression or "<" in expression or "<>" in expression or ">=" in expression or "<=" in expression:
        # Extract the operands and the operator
        operands = expression.split()
        operator = operands[1]
        # Evaluate the operands recursively
        op1 = eval_expression(operands[0], variables)
        op2 = eval_expression(operands[2], variables)
        # Perform the comparison
        if operator == "=":
            return op1 == op2
        elif operator == ">":
            return op1 > op2
        elif operator == "<":
            return op1 < op2
        elif operator == "<>":
            return op1 != op2
        elif operator == ">=":
            return op1 >= op2
        elif operator == "<=":
            return op1 <= op2
    # If the expression is not recognized, return None
    return None

if __name__ == '__main__':
    # Read the program from stdin
    program = [line.strip() for line in sys.stdin]
    # Interpret the program
    variables = interpret_basic(program)
    # Print the variables dictionary
    print(variables)

