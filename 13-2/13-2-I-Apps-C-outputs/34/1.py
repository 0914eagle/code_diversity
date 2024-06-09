
def interpret_basic(program):
    # Initialize the variables
    variables = {}
    for line in program:
        # Split the line into label and statement
        label, statement = line.split()
        # Convert the label to an integer
        label = int(label)
        # Check if the statement is a LET statement
        if statement.startswith("LET"):
            # Extract the variable name and value
            variable_name, value = statement.split("=")
            # Convert the value to an integer
            value = int(value)
            # Assign the value to the variable
            variables[variable_name] = value
        # Check if the statement is a PRINT statement
        elif statement.startswith("PRINT"):
            # Extract the print statement
            print_statement = statement.split("PRINT")[1]
            # Print the statement
            print(print_statement, end="")
        # Check if the statement is a PRINTLN statement
        elif statement.startswith("PRINTLN"):
            # Extract the print statement
            print_statement = statement.split("PRINTLN")[1]
            # Print the statement with a newline
            print(print_statement)
        # Check if the statement is an IF statement
        elif statement.startswith("IF"):
            # Extract the condition and label
            condition, label = statement.split("THEN")
            # Convert the label to an integer
            label = int(label)
            # Evaluate the condition
            if eval(condition):
                # Go to the label if the condition is true
                label = label
            else:
                # Continue to the next statement if the condition is false
                label = label + 1
        # Check if the statement is a GOTO statement
        elif statement.startswith("GOTO"):
            # Extract the label
            label = int(statement.split("GOTO")[1])
        # Update the current label
        current_label = label
    return variables

