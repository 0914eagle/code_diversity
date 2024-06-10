
def remove_extra_zeros(number):
    number = number.lstrip('0').rstrip('0')
    if number.startswith('.'):
        number = '0' + number
    return number

def convert_to_simple_exponential_notation(x):
    x = remove_extra_zeros(x)
    decimal_index = x.find('.')
    if decimal_index == -1:
        a = x
        b = 0
    else:
        a = x.replace('.', '')
        b = decimal_index - len(x) + 1
    result = f"{a}E{b}" if b != 0 else a
    return result

if __name__ == "__main__":
    x = input().strip()
    print(convert_to_simple_exponential_notation(x))
