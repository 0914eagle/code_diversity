
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

    # Divide the coefficients by the least common multiple
    for sign in elements.keys():
        elements[sign] = {k: v // lcm for k, v in elements[sign].items()}
        coefficients[sign] //= lcm

    # Find the minimum number of each element needed to balance the equation
    min_elements = {}
    for element in elements["+1"].keys():
        min_elements[element] = total_coefficients // elements["+1"][element]

    # Return the minimum number of each element needed to balance the equation
    return [min_elements[element] for element in sorted(min_elements.keys())]

def find_lcm(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while True:
        a, b = b, a % b
        if b == 0:
            return a
