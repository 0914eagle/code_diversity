
def convert_to_celsius(fahrenheit):
    numerator, denominator = fahrenheit.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    celsius = (numerator - 32) * 5 // 9
    gcd = find_gcd(celsius, denominator)
    return f"{celsius // gcd}/{denominator // gcd}"

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

fahrenheit = input()
print(convert_to_celsius(fahrenheit))

