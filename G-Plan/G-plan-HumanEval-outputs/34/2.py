
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Main function to read input and call filter_integers function
def main():
    values = input().strip().split(',')
    values = [eval(value) for value in values]  # Evaluate input values
    result = filter_integers(values)
    print(result)

if __name__ == "__main__":
    main()
