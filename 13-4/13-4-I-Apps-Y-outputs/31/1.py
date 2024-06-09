
def solve(input_string):
    output_string = ""
    for i in range(len(input_string)):
        if input_string[i] == "<":
            if i > 0 and input_string[i-1] != "<":
                output_string = output_string[:-1]
        else:
            output_string += input_string[i]
    return output_string

