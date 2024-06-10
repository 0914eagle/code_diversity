
def multiply(a: int, b: int) -> int:
    return abs(a % 10) * abs(b % 10)

# Main function to read input and call the multiply function
if __name__ == "__main__":
    a, b = map(int, input().split())
    result = multiply(a, b)
    print(result)
