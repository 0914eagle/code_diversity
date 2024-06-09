
def solve(n, data):
    # Initialize a dictionary to store the input values
    inputs = {}
    # Initialize a dictionary to store the output values
    outputs = {}
    # Iterate over the input data
    for i in range(n):
        # Split the current line into words
        words = data[i].split()
        # Check if the current vertex is an input vertex
        if words[0] == "IN":
            # If it is an input vertex, add it to the inputs dictionary with the given value
            inputs[i] = int(words[1])
        else:
            # If it is a logical element, add it to the outputs dictionary with the given inputs
            outputs[i] = [int(x) for x in words[1:]]
    # Initialize a list to store the answers
    answer = []
    # Iterate over the inputs
    for i in inputs:
        # Create a copy of the inputs dictionary
        curr_inputs = inputs.copy()
        # Change the value of the current input to 0
        curr_inputs[i] = 0
        # Initialize a flag to indicate if the output is 1
        is_one = True
        # Iterate over the outputs
        for j in outputs:
            # If the current output is not 1, set the flag to False
            if outputs[j][0] != 1 or (len(outputs[j]) > 1 and outputs[j][1] != curr_inputs[outputs[j][1]]):
                is_one = False
                break
        # If the flag is True, add a 1 to the answer, otherwise add a 0
        answer.append(1 if is_one else 0)
    # Return the answer
    return "".join(str(x) for x in answer)

