
def solve(numbers):
    for operation in "+-*/":
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j and eval(" ".join(map(str, numbers[:i] + [operation] + numbers[i:j] + numbers[j:]))) == int(numbers[j]):
                    return " ".join(map(str, numbers[:i] + [operation] + numbers[i:j] + numbers[j:]))

