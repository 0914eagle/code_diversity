
def is_beautiful_sequence(numbers):
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) != 1:
            return False
    return True

def construct_beautiful_sequence(a, b, c, d):
    numbers = []
    for i in range(a):
        numbers.append(0)
    for i in range(b):
        numbers.append(1)
    for i in range(c):
        numbers.append(2)
    for i in range(d):
        numbers.append(3)
    return numbers

def main():
    a, b, c, d = map(int, input().split())
    numbers = construct_beautiful_sequence(a, b, c, d)
    if is_beautiful_sequence(numbers):
        print("YES")
        print(" ".join(map(str, numbers)))
    else:
        print("NO")

if __name__ == "__main__":
    main()

