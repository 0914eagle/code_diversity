
def get_unique_results(numbers):
    results = set()
    for a, b in numbers:
        for op in ["+", "-", "*"]:
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            else:
                result = a * b
            if result not in results:
                results.add(result)
                yield a, op, b, "=", result

def main():
    n = int(input())
    numbers = []
    for _ in range(n):
        a, b = map(int, input().split())
        numbers.append((a, b))
    for result in get_unique_results(numbers):
        print(*result)

if __name__ == '__main__':
    main()

