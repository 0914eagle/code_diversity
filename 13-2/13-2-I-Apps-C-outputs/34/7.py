
def interpret(program):
    # Initialize variables
    variables = {}
    for line in program:
        # Split the line into label and statement
        label, statement = line.split()
        # Convert label to integer
        label = int(label)
        # Check if the statement is a LET statement
        if statement.startswith("LET"):
            # Extract the variable name and value
            variable_name, value = statement.split("=")
            # Evaluate the value
            value = eval_expression(value.strip())
            # Assign the value to the variable
            variables[variable_name] = value
        # Check if the statement is a PRINT or PRINTLN statement
        elif statement.startswith("PRINT"):
            # Extract the print statement
            print_statement = statement.split("PRINT")[1].strip()
            # Evaluate the print statement
            print_statement = eval_expression(print_statement)
            # Print the statement
            print(print_statement, end="")
        elif statement.startswith("PRINTLN"):
            # Extract the print statement
            print_statement = statement.split("PRINTLN")[1].strip()
            # Evaluate the print statement
            print_statement = eval_expression(print_statement)
            # Print the statement with a newline
            print(print_statement)
        # Check if the statement is an IF statement
        elif statement.startswith("IF"):
            # Extract the condition and label
            condition, label = statement.split("THEN")
            # Evaluate the condition
            condition = eval_expression(condition.strip())
            # Check if the condition is true
            if condition:
                # Go to the label
                label = int(label.strip())
                break
        # Check if the statement is a GOTO statement
        elif statement.startswith("GOTO"):
            # Extract the label
            label = int(statement.split("GOTO")[1].strip())
            # Break the loop and go to the label
            break
    # Return the variables and the label
    return variables, label

def eval_expression(expression):
    # Evaluate the expression
    result = eval(expression)
    # Check if the result is a string
    if isinstance(result, str):
        # Return the string
        return result
    # Check if the result is an integer
    elif isinstance(result, int):
        # Return the integer
        return result
    # Check if the result is a variable
    elif result in variables:
        # Return the variable value
        return variables[result]
    # Otherwise, return 0
    else:
        return 0

if __name__ == '__main__':
    # Read the program from stdin
    program = [line.strip() for line in sys.stdin]
    # Interpret the program
    variables, label = interpret(program)
    # Print the variables and the label
    print(variables)
    print(label)

