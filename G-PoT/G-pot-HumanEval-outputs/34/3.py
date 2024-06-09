
def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    if a == b:
        return None
    if isinstance(a, str):
        a = a.replace(',', '.') if ',' in a else float(a)
    if isinstance(b, str):
        b = b.replace(',', '.') if ',' in b else float(b)
    
    if isinstance(a, int) and isinstance(b, int):
        return None if a == b else max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return None if a == b else max(a, b)
    else:
        return b if isinstance(b, (float, int)) else a
