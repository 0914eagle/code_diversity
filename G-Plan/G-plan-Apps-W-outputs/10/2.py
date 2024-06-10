
def remove_extra_zeros(num_str):
    num_str = num_str.lstrip('0').rstrip('0')
    if num_str.startswith('.'):
        num_str = '0' + num_str
    return num_str

def convert_to_simple_exponential(num_str):
    num_str = remove_extra_zeros(num_str)
    decimal_pos = num_str.find('.')
    a = num_str.replace('.', '')
    b = decimal_pos - len(a) + 1 if decimal_pos != -1 else 0
    result = f"{a}E{b}" if b != 0 else a
    return result

if __name__ == "__main__":
    x = input().strip()
    print(convert_to_simple_exponential(x))
