
def balanced_equation(equation):
    # Initialize a dictionary to store the elements and their counts
    elements = {}
    
    # Iterate over the equation and populate the dictionary
    for molecule in equation:
        for element, count in molecule:
            if element not in elements:
                elements[element] = count
            else:
                elements[element] += count
    
    # Find the least common multiple (LCM) of the counts for each element
    lcm = 1
    for count in elements.values():
        lcm = lcm_of_two_numbers(lcm, count)
    
    # Divide each count by the LCM to get the balanced counts
    balanced_equation = []
    for element, count in elements.items():
        balanced_equation.append(count // lcm)
    
    return balanced_equation

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

