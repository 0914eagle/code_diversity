
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Main function to read input and call filter_integers
def main():
    values = input().strip().split(',')
    values = [eval(val) for val in values]  # Evaluate input strings to actual Python objects
    result = filter_integers(values)
    print(result)

if __name__ == "__main__":
    main()
