
def balanced_equation(equation):
    # Initialize a dictionary to store the elements and their counts
    elements = {}
    
    # Iterate over the equation and parse the input
    for line in equation:
        if line == "0 0":
            break
        sign, num_elements = line.split(" ")
        num_elements = int(num_elements)
        for i in range(num_elements):
            element, count = line.split(" ")
            count = int(count)
            if element not in elements:
                elements[element] = 0
            elements[element] += count if sign == "+" else -count
    
    # Find the least common multiple (LCM) of the counts for each element
    lcm = 1
    for count in elements.values():
        lcm = lcm_of_two_numbers(lcm, count)
    
    # Divide the counts for each element by the LCM to get the balanced counts
    balanced_elements = {}
    for element, count in elements.items():
        balanced_elements[element] = count // lcm
    
    # Return the balanced counts in the order of the input equation
    return [balanced_elements[element] for element in equation if element != "0 0"]

def lcm_of_two_numbers(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while(True):
        if(greater % x == 0 and greater % y == 0):
            lcm = greater
            break
        greater += 1
    
    return lcm

