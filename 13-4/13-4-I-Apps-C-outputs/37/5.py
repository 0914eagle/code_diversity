
def f1(n):
    # function to generate all possible combinations of numbers and operators
    def generate_combinations(n):
        nums = [i for i in range(1, 10)]
        ops = ["+", "-", "*"]
        combinations = []
        for i in range(n):
            for num1 in nums:
                for num2 in nums:
                    for op in ops:
                        combinations.append([num1, num2, op])
        return combinations
    
    # function to check if the result of an equation is unique
    def is_unique(result, results):
        if result not in results:
            results.append(result)
            return True
        else:
            return False
    
    # function to generate a valid equation
    def generate_equation(combination):
        num1, num2, op = combination
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        else:
            result = num1 * num2
        return f"{num1} {op} {num2} = {result}"
    
    # main function
    results = []
    combinations = generate_combinations(n)
    for combination in combinations:
        equation = generate_equation(combination)
        if is_unique(equation, results):
            yield equation
        else:
            continue

def f2(n):
    # function to read input and call f1
    nums = []
    for _ in range(n):
        num1, num2 = map(int, input().split())
        nums.append([num1, num2])
    for equation in f1(n):
        print(equation)

if __name__ == '__main__':
    n = int(input())
    f2(n)

