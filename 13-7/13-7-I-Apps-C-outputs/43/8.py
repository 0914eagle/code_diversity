
def get_expression(expression):
    return expression.split('+')

def get_variable_value(expression, variable):
    return int(expression.split(variable)[0])

def get_remainder(expression, variable, modulo):
    return int(expression.split(variable)[1]) % modulo

def solve(expression, p, m):
    variable = 'x'
    min_value = 0
    max_value = 100000
    while min_value <= max_value:
        mid_value = (min_value + max_value) // 2
        if get_remainder(expression, variable, mid_value) == p:
            min_value = mid_value + 1
        else:
            max_value = mid_value - 1
    return min_value

if __name__ == '__main__':
    expression = input()
    p, m = map(int, input().split())
    print(solve(expression, p, m))

