
def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    if isinstance(a, str) and ',' in a:
        a = float(a.replace(',', '.'))
    if isinstance(b, str) and ',' in b:
        b = float(b.replace(',', '.'))

    if a == b:
        return None
    elif isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b, key=float)
    elif isinstance(a, int) and isinstance(b, float):
        return max(float(a), b)
    elif isinstance(a, float) and isinstance(b, int):
        return max(a, float(b))
    elif isinstance(a, int) and isinstance(b, str):
        return max(float(a), b, key=float)
    elif isinstance(a, str) and isinstance(b, int):
        return max(a, float(b), key=float)
    elif isinstance(a, float) and isinstance(b, str):
        return max(a, float(b))
