
def generate_exam(n):
    # Generate a list of unique pairs of numbers
    pairs = [(a, b) for a in range(-10**6, 10**6) for b in range(-10**6, 10**6) if a != b]
    pairs = list(set(pairs))[:n]

    # Generate a list of unique results
    results = set()
    while len(results) < n:
        a, b = pairs.pop()
        results.add(a + b)
        results.add(a * b)
        results.add(a - b)

    # Generate the exam
    exam = []
    for a, b in pairs:
        for op in ['+', '*', '-']:
            if eval(f'{a} {op} {b}') in results:
                exam.append(f'{a} {op} {b} = {eval(f"{a} {op} {b}")}')
                results.remove(eval(f'{a} {op} {b}'))
                break

    return exam

def main():
    n = int(input())
    print('\n'.join(generate_exam(n)))

if __name__ == '__main__':
    main()

