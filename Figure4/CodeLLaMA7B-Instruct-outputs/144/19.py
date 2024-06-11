

def simplify(x, n):
    

    # Convert the strings to fractions
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    # Multiply the numerators and denominators
    product_numerator = int(x_numerator) * int(n_numerator)
    product_denominator = int(x_denominator) * int(n_denominator)

    # Check if the result is a whole number
    if product_numerator % product_denominator == 0:
        return True
    else:
        return False

# Test cases
print(
