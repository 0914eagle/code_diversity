
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
            # Evaluate the value
            value = eval_expression(var_value.strip())
            # Assign the value to the variable
            variables[var_name] = value
        # Check if the statement is a PRINT statement
        elif statement.startswith("PRINT"):
            # Extract the print statement
            print_statement = statement.split("PRINT")[1].strip()
            # Evaluate the print statement
            value = eval_expression(print_statement)
            # Print the value
            print(value, end="")
        # Check if the statement is a PRINTLN statement
        elif statement.startswith("PRINTLN"):
            # Extract the print statement
            print_statement = statement.split("PRINTLN")[1].strip()
            # Evaluate the print statement
            value = eval_expression(print_statement)
            # Print the value with a newline
            print(value)
        # Check if the statement is a GOTO statement
        elif statement.startswith("GOTO"):
            # Extract the label
            label = statement.split("GOTO")[1].strip()
            # Find the line with the label
            for line in program:
                if line.startswith(label):
                    # Set the current line to the line with the label
                    current_line = line
                    break
    return variables

def eval_expression(expression):
    # Evaluate the expression using the variables
    return eval(expression, variables)

if __name__ == '__main__':
    # Read the program from stdin
    program = [line.strip() for line in sys.stdin.readlines()]
    # Interpret the program
    variables = interpret_basic(program)
    # Print the variables
    for var_name, value in variables.items():
        print(f"{var_name} = {value}")

