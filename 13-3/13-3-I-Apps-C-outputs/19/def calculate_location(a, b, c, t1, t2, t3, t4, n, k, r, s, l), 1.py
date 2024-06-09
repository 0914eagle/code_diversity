
import math

def calculate_location(a, b, c, t1, t2, t3, t4, n, k, r, s, l):
    # Calculate the Taylor polynomial of degree r around 0
    p = taylor_polynomial(a, b, c, t1, t2, t3, t4, r)
    
    # Create a sequence of polynomials by recursively adding the previous polynomial to itself
    p_seq = [p]
    for i in range(n):
        p_seq.append(sum_polynomials(p_seq[i], p, r + i + 1))
    
    # Differentiate the final polynomial in the sequence and add l to the result
    g = differentiate_polynomial(p_seq[-1], r + s + 1) + l
    
    # Calculate the location of the opponent
    location = (g**2 / math.pi / math.e) + (1 / (l + 1))
    
    return location

def taylor_polynomial(a, b, c, t1, t2, t3, t4, r):
    # Calculate the integral of the function f(x) from a to b
    integral = integrate_function(a, b, c, t1, t2, t3, t4)
    
    # Calculate the r-th degree Taylor polynomial of f(x) around 0
    p = taylor_polynomial_coefficients(integral, r)
    
    return p

def integrate_function(a, b, c, t1, t2, t3, t4):
    # Calculate the integral of the function f(x) from a to b
    integral = c * math.log(b) - c * math.log(a) + t1 * math.gamma(b) - t1 * math.gamma(a) + t2 * math.sqrt(math.log(b)) - t2 * math.sqrt(math.log(a)) - t3 * math.erf(b) + t3 * math.erf(a) + t4 * math.jn(b, x) - t4 * math.jn(a, x)
    
    return integral

def taylor_polynomial_coefficients(integral, r):
    # Calculate the coefficients of the Taylor polynomial of degree r
    coefficients = [integral]
    for i in range(1, r + 1):
        coefficients.append(coefficients[i - 1] / (i + 1))
    
    return coefficients

def sum_polynomials(p1, p2, r):
    # Sum the coefficients of the two polynomials
    summed_coefficients = [p1[i] + p2[i] for i in range(r + 1)]
    
    return summed_coefficients

def differentiate_polynomial(p, r):
    # Differentiate the polynomial p of degree r
    differentiated_coefficients = [i * p[i] for i in range(1, r + 1)]
    
    return differentiated_coefficients

def main():
    a, b, c, t1, t2, t3, t4, n, k, r, s, l = map(int, input().split())
    location = calculate_location(a, b, c, t1, t2, t3, t4, n, k, r, s, l)
    print(location)

if __name__ == "__main__":
    main()

