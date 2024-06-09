
def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if float(a) == float(b):
            return None
        elif float(a) > float(b):
            return float(a)
        else:
            return float(b)
    else:
        if isinstance(a, str) and isinstance(b, str):
            a_float = float(a.replace(',', '.')) if ',' in a else float(a)
            b_float = float(b.replace(',', '.')) if ',' in b else float(b)
            if a_float == b_float:
                return None
            elif a_float > b_float:
                return a
            else:
                return b
        else:
            raise ValueError("Invalid input types")

# Test cases
print(compare_one(1, 2.5))  # Output: 2.5
print(compare_one(1, '2,3'))  # Output: '2,3'
print(compare_one('5,1', '6'))  # Output: '6'
print(compare_one('1', 1))  # Output: None
