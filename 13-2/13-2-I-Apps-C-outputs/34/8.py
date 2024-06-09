
def interpret_basic(program):
    # Initialize the variables
    variables = {}
    for line in program:
        # Split the line into label and command
        label, command = line.split()
        # Convert the label to an integer
        label = int(label)
        # Check if the command is LET
        if command.startswith("LET"):
            # Extract the variable name and value
            variable_name, value = command.split("=")
            # Evaluate the value
            value = eval_expression(value.strip())
            # Assign the value to the variable
            variables[variable_name] = value
        # Check if the command is IF
        elif command.startswith("IF"):
            # Extract the condition
            condition = command.split("THEN")[0].strip()
            # Evaluate the condition
            condition = eval_expression(condition)
            # Check if the condition is true
            if condition:
                # Extract the label
                label = command.split("THEN")[1].strip()
                # Jump to the label
                label = int(label)
                break
        # Check if the command is PRINT or PRINTLN
        elif command.startswith(("PRINT", "PRINTLN")):
            # Extract the print statement
            print_statement = command.split(maxsplit=1)[1]
            # Evaluate the print statement
            print_statement = eval_expression(print_statement.strip())
            # Print the statement
            if command.startswith("PRINT"):
                print(print_statement, end="")
            else:
                print(print_statement)
    return variables

def eval_expression(expression):
    # Evaluate the expression using the variables
    return eval(expression, variables)

if __name__ == '__main__':
    # Read the program from stdin
    program = [line.strip() for line in sys.stdin]
    # Interpret the program
    variables = interpret_basic(program)
    # Print the variables
    for variable, value in variables.items():
        print(f"{variable} = {value}")

