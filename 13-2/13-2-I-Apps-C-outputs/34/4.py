
def interpret(program):
    # Initialize the variables
    variables = {}
    for line in program:
        # Split the line into label and statement
        label, statement = line.split()
        # Check if the statement is a LET statement
        if statement.startswith("LET"):
            # Extract the variable name and value
            var_name, var_value = statement.split("=")
            # Evaluate the value and assign it to the variable
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
    # Evaluate the expression using the variables dictionary
    return eval(expression, variables)

if __name__ == '__main__':
    # Test the interpreter with the sample input
    program = ["10 LET A = 1", "20 PRINT \"HELLO THERE \"", "30 PRINTLN A", "40 LET A = A + 1", "50 IF A <= 5 THEN GOTO 20", "60 PRINTLN \"DONE\""]
    variables = interpret(program)
    print(variables)

