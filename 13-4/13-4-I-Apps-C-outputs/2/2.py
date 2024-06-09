
def is_beautiful_sequence(numbers):
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) != 1:
            return False
    return True

def get_beautiful_sequence(a, b, c, d):
    numbers = [0] * a + [1] * b + [2] * c + [3] * d
    if is_beautiful_sequence(numbers):
        return "YES\n" + " ".join(map(str, numbers))
    else:
        return "NO"

