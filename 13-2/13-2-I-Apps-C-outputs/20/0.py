
def balanced_equation(equation):
    # Initialize variables
    elements = {}
    coefficients = {}
    total_coefficients = 0

    # Parse the equation
    for line in equation:
        if line == "0 0":
            break
        sign, num_elements = line.split(" ")
        num_elements = int(num_elements)
        elements[sign] = {}
        coefficients[sign] = 1
        for i in range(num_elements):
            element, count = line.split(" ")
            elements[sign][element] = int(count)
            total_coefficients += int(count)

    # Find the least common multiple of the coefficients
    lcm = 1
    for coefficient in coefficients.values():
        lcm = find_lcm(lcm, coefficient)

    # Fill in the blanks in the equation
    output = []
    for sign in ["+1", "-1"]:
        for element in elements[sign]:
            count = elements[sign][element] * lcm // coefficients[sign]
            output.append(str(count))
    return " ".join(output)

def find_lcm(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while True:
        a, b = b, a % b
        if b == 0:
            return a

