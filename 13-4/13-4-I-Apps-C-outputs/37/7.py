
def f1(n):
    # function to generate a list of unique pairs of numbers
    def generate_pairs(n):
        pairs = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    pairs.append((i, j))
        return pairs
    
    # function to generate a list of unique equations
    def generate_equations(pairs):
        equations = []
        for pair in pairs:
            a, b = pair
            equations.append(str(a) + " + " + str(b) + " = " + str(a+b))
            equations.append(str(a) + " - " + str(b) + " = " + str(a-b))
            equations.append(str(a) + " * " + str(b) + " = " + str(a*b))
        return equations
    
    # function to check if the list of equations is unique
    def is_unique(equations):
        unique_equations = []
        for equation in equations:
            if equation not in unique_equations:
                unique_equations.append(equation)
        return len(unique_equations) == len(equations)
    
    # generate a list of unique pairs of numbers
    pairs = generate_pairs(n)
    
    # generate a list of unique equations
    equations = generate_equations(pairs)
    
    # check if the list of equations is unique
    if is_unique(equations):
        return equations
    else:
        return ["impossible"]

def f2(n):
    # function to generate a list of unique pairs of numbers
    def generate_pairs(n):
        pairs = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    pairs.append((i, j))
        return pairs
    
    # function to generate a list of unique equations
    def generate_equations(pairs):
        equations = []
        for pair in pairs:
            a, b = pair
            equations.append(str(a) + " + " + str(b) + " = " + str(a+b))
            equations.append(str(a) + " - " + str(b) + " = " + str(a-b))
            equations.append(str(a) + " * " + str(b) + " = " + str(a*b))
        return equations
    
    # function to check if the list of equations is unique
    def is_unique(equations):
        unique_equations = []
        for equation in equations:
            if equation not in unique_equations:
                unique_equations.append(equation)
        return len(unique_equations) == len(equations)
    
    # generate a list of unique pairs of numbers
    pairs = generate_pairs(n)
    
    # generate a list of unique equations
    equations = generate_equations(pairs)
    
    # check if the list of equations is unique
    if is_unique(equations):
        return equations
    else:
        return ["impossible"]

if __name__ == '__main__':
    n = int(input())
    pairs = []
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    equations = f1(n)
    for equation in equations:
        print(equation)

