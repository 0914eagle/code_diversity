
def solve(n, data):
    # Initialize a dictionary to store the inputs and their values
    inputs = {}
    for i in range(n):
        inputs[i+1] = None

    # Iterate through the data and create a graph representing the logical scheme
    graph = {}
    for row in data:
        vertex_type, *vertex_inputs = row.split()
        vertex_inputs = [int(input) for input in vertex_inputs]
        graph[i] = (vertex_type, vertex_inputs)

    # Function to evaluate the output of a vertex
    def evaluate(vertex):
        vertex_type, vertex_inputs = graph[vertex]
        if vertex_type == "IN":
            return inputs[vertex]
        elif vertex_type == "AND":
            return all(inputs[input] for input in vertex_inputs)
        elif vertex_type == "OR":
            return any(inputs[input] for input in vertex_inputs)
        elif vertex_type == "XOR":
            return any(inputs[input] for input in vertex_inputs) and not all(inputs[input] for input in vertex_inputs)
        elif vertex_type == "NOT":
            return not inputs[vertex_inputs[0]]

    # Initialize the output string
    output = ""

    # Iterate through the inputs and evaluate the output for each input
    for input_vertex in range(1, n+1):
        inputs[input_vertex] = 0
        output += str(evaluate(n))
        inputs[input_vertex] = 1
        output += str(evaluate(n))

    return output

