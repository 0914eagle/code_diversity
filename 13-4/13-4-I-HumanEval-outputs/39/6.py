
from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
    
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list is not equal to the length of operand list minus one.")

    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == "+":
            result += operand[i + 1]
        elif operator[i] == "-":
            result -= operand[i + 1]
        elif operator[i] == "*":
            result *= operand[i + 1]
        elif operator[i] == "//":
            result //= operand[i + 1]
        elif operator[i] == "**":
            result **= operand[i + 1]
        else:
            raise ValueError("Invalid operator.")

    return result

