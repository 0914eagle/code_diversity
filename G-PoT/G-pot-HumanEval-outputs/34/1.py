
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
    elif isinstance(a, str) and isinstance(b, str):
        a_float = float(a.replace(',', '.')) if ',' in a else float(a)
        b_float = float(b.replace(',', '.')) if ',' in b else float(b)
        if a_float == b_float:
            return None
        elif a_float > b_float:
            return a
        else:
            return b
    else:
        return None
