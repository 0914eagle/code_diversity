
def truncate_number(number: float) -> float:
    return number % 1

if __name__ == "__main__":
    number = float(input().strip())
    result = truncate_number(number)
    print(result)
