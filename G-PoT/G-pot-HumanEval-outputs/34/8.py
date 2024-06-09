
def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    if isinstance(a, str) and ',' in a:
        a = float(a.replace(',', '.'))
    if isinstance(b, str) and ',' in b:
        b = float(b.replace(',', '.'))

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b
