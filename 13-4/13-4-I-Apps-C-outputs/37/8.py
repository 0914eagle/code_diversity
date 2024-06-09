
def f1(n):
    # function to generate all possible equations
    def generate_equations(n):
        equations = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                for op in ['+', '-', '*']:
                    equations.append((i, op, j))
        return equations
    
    # function to check if the result of an equation is unique
    def is_unique(equations, result):
        for equation in equations:
            if eval(equation) == result:
                return False
        return True
    
    # generate all possible equations
    equations = generate_equations(n)
    
    # shuffle the equations to randomize the order
    import random
    random.shuffle(equations)
    
    # iterate through the equations and check if the result is unique
    for equation in equations:
        result = eval(equation)
        if is_unique(equations, result):
            return equation
    
    # if no unique result is found, return "impossible"
    return "impossible"

def f2(n, a, b):
    # function to check if a pair of numbers is valid
    def is_valid(a, b):
        return a >= -10**6 and a <= 10**6 and b >= -10**6 and b <= 10**6
    
    # check if the pair of numbers is valid
    if not is_valid(a, b):
        return "impossible"
    
    # generate all possible equations for the pair of numbers
    equations = [(a, op, b) for op in ['+', '-', '*']]
    
    # shuffle the equations to randomize the order
    import random
    random.shuffle(equations)
    
    # iterate through the equations and check if the result is unique
    for equation in equations:
        result = eval(equation)
        if is_unique(equations, result):
            return equation
    
    # if no unique result is found, return "impossible"
    return "impossible"

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(f2(n, a, b))

