
import random

def evaluate_expression(expression):
    integers = expression.split("+")
    total = 0
    for i in range(len(integers)):
        if i % 2 == 0:
            total += int(integers[i])
        else:
            total = str(total) + integers[i]
    return total

def count_distinct_integers(expression):
    integers = expression.split("+")
    distinct_integers = set()
    for i in range(len(integers)):
        if i % 2 == 0:
            distinct_integers.add(int(integers[i]))
        else:
            distinct_integers.add(str(distinct_integers.pop()) + integers[i])
    return len(distinct_integers)

def main():
    expression = input("Enter an expression: ")
    print(f"The expression evaluates to {evaluate_expression(expression)} in DPG.")
    print(f"The number of distinct integers the expression can evaluate to is {count_distinct_integers(expression)}.")

if __name__ == '__main__':
    main()

