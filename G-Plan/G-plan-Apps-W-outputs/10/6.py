
def remove_extra_zeros(num_str):
    num_str = num_str.lstrip('0')
    if num_str.startswith('.'):
        num_str = '0' + num_str
    num_str = num_str.rstrip('0')
    if num_str.endswith('.'):
        num_str = num_str[:-1]
    return num_str

def convert_to_simple_exponential(num_str):
    decimal_point_index = num_str.find('.')
    if decimal_point_index == -1:
        a = num_str
        b = 0
    else:
        a = num_str.replace('.', '')
        b = decimal_point_index - len(num_str) + 1
    if a.startswith('0'):
        a = a[1:]
    if a == '':
        a = '0'
    if b == 0:
        return a
    return f"{a}E{b}"

if __name__ == "__main__":
    x = input().strip()
    x = remove_extra_zeros(x)
    result = convert_to_simple_exponential(x)
    print(result)
