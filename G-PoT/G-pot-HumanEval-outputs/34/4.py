
def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    if type(a) == type(b):
        if a == b:
            return None
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        a_num = float(a.replace(',', '.')) if ',' in a else float(a)
        b_num = float(b.replace(',', '.')) if ',' in b else float(b)
        if a_num == b_num:
            return None
        return a if a_num > b_num else b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        return a if a > b else b
    else:
        return None
