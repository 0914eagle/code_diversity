
def parse_expression(expression):
    # Function to parse the expression and return a list of numbers and operators
    numbers = []
    operators = []
    for char in expression:
        if char.isdigit():
            numbers.append(int(char))
        elif char in ["+", "-"]:
            operators.append(char)
    return numbers, operators


def evaluate_expression(numbers, operators):
    # Function to evaluate the expression and return the result
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        else:
            result -= numbers[i + 1]
    return result


def get_maximum_value(expression, plus_count, minus_count):
    # Function to get the maximum value of the expression after placing the plus and minus operators
    numbers, operators = parse_expression(expression)
    plus_indices = [i for i in range(len(numbers)) if numbers[i] == 1]
    minus_indices = [i for i in range(len(numbers)) if numbers[i] == -1]
    max_value = 0
    for plus_index in plus_indices:
        for minus_index in minus_indices:
            numbers[plus_index] = 0
            numbers[minus_index] = 0
            result = evaluate_expression(numbers, operators)
            if result > max_value:
                max_value = result
            numbers[plus_index] = 1
            numbers[minus_index] = -1
    return max_value


if __name__ == "__main__":
    expression = input()
    plus_count, minus_count = map(int, input().split())
    print(get_maximum_value(expression, plus_count, minus_count))

