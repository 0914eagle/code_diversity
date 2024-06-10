
def remove_extra_zeros(num_str):
    num_str = num_str.lstrip('0')
    if num_str.startswith('.'):
        num_str = '0' + num_str
    return num_str

def convert_to_simple_exponential(num_str):
    num_str = remove_extra_zeros(num_str)
    decimal_index = num_str.index('.')
    a = num_str.replace('.', '')
    b = decimal_index - len(a) + 1
    if b == 0:
        result = f"{a}E{b}"
    else:
        result = f"{a[0]}.{a[1:]}E{b}"
    return result

if __name__ == "__main__":
    x = input().strip()
    print(convert_to_simple_exponential(x))
