
def parse_expression(expression):
    # Function to parse the expression and return a tuple of numbers and operators
    numbers = []
    operators = []
    for char in expression:
        if char.isdigit():
            numbers.append(int(char))
        elif char in "+-":
            operators.append(char)
    return numbers, operators


def evaluate_expression(numbers, operators):
    # Function to evaluate the expression and return the result
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i+1]
        else:
            result -= numbers[i+1]
    return result


def find_max_value(numbers, operators, plus_count, minus_count):
    # Function to find the maximum value of the expression by trying all possible combinations of plus and minus operators
    max_value = 0
    for plus_indices in combinations(range(len(numbers)-1), plus_count):
        for minus_indices in combinations(range(1, len(numbers)), minus_count):
            current_operators = []
            for i in range(len(numbers)-1):
                if i in plus_indices:
                    current_operators.append("+")
                elif i in minus_indices:
                    current_operators.append("-")
                else:
                    current_operators.append(operators[i])
            current_value = evaluate_expression(numbers, current_operators)
            if current_value > max_value:
                max_value = current_value
    return max_value


def main():
    expression = input()
    numbers, operators = parse_expression(expression)
    plus_count, minus_count = map(int, input().split())
    max_value = find_max_value(numbers, operators, plus_count, minus_count)
    print(max_value)


if __name__ == "__main__":
    main()

