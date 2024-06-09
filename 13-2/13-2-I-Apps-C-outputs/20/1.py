
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
        elements[sign] = []
        coefficients[sign] = []
        for i in range(num_elements):
            element, count = line.split(" ")
            elements[sign].append(element)
            coefficients[sign].append(int(count))

    # Calculate the total number of coefficients
    for sign in ["+1", "-1"]:
        for element, count in zip(elements[sign], coefficients[sign]):
            if element not in elements:
                elements[element] = 0
            elements[element] += count
            total_coefficients += count

    # Calculate the minimum number of coefficients for each element
    min_coefficients = {}
    for element, count in elements.items():
        min_coefficients[element] = count // total_coefficients

    # Fill in the blanks in the equation
    coefficients_list = []
    for sign in ["+1", "-1"]:
        for element, count in zip(elements[sign], coefficients[sign]):
            if element not in min_coefficients:
                continue
            coefficients_list.append(str(min_coefficients[element] * count))

    return " ".join(coefficients_list)

