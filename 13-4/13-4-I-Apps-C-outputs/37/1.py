
def get_input():
    n = int(input())
    pairs = []
    for i in range(n):
        pair = input().split()
        pairs.append((int(pair[0]), int(pair[1])))
    return n, pairs

def get_unique_results(pairs):
    results = set()
    for pair in pairs:
        for operator in ["+", "-", "*"]:
            result = eval(f"{pair[0]} {operator} {pair[1]}")
            if result not in results:
                results.add(result)
                break
    return results

def generate_equations(pairs, results):
    equations = []
    for pair in pairs:
        for operator in ["+", "-", "*"]:
            result = eval(f"{pair[0]} {operator} {pair[1]}")
            if result in results:
                equations.append(f"{pair[0]} {operator} {pair[1]} = {result}")
                results.remove(result)
                break
    return equations

def main():
    n, pairs = get_input()
    results = get_unique_results(pairs)
    equations = generate_equations(pairs, results)
    for equation in equations:
        print(equation)

if __name__ == '__main__':
    main()

