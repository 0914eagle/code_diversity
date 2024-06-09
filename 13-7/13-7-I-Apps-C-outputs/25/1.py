
import math

def calculate_location(a, b, c, t1, t2, t3, t4, n, k, r, s, l):
    # Calculate the Taylor polynomial of degree r around 0
    p = taylor_polynomial(a, b, c, t1, t2, t3, t4, r)
    
    # Calculate the sequence of polynomials P_n(x) = sum(P_{n-1}(i) * x^i)
    p_seq = [p]
    for i in range(n):
        p_seq.append(sum(p_seq[i] * x**i for i in range(r+1+i)))
    
    # Calculate the final polynomial g(x) = (P_s(x) + l)^2 / (pi * e) + 1 / (l + 1)
    g = (p_seq[s] + l)**2 / math.pi / math.e + 1 / (l + 1)
    
    # Return the location of the opponent
    return g

def taylor_polynomial(a, b, c, t1, t2, t3, t4, r):
    # Calculate the integral of the function f(x) = c * int_a^b (t1 * gamma(x) + sqrt(t2 * log(erf(t3 * x)) - J_k(x)^t4) * dx
    f = c * integrate(a, b, t1, t2, t3, t4)
    
    # Calculate the Taylor polynomial of degree r around 0
    return sum(f.subs(x, x**i / factorial(i)) for i in range(r+1))

def integrate(a, b, t1, t2, t3, t4):
    # Calculate the integral of the function inside the parentheses
    integral = t1 * math.gamma(x) + math.sqrt(t2 * math.log(math.erf(t3 * x)) - J_k(x)**t4)
    
    # Return the result of the integral
    return integrate.doit()

def J_k(x):
    # Calculate the Bessel function of the first kind
    return math.sin(k * x) / math.pi

if __name__ == "__main__":
    a, b, c, t1, t2, t3, t4, n, k, r, s, l = map(float, input().split())
    print(calculate_location(a, b, c, t1, t2, t3, t4, n, k, r, s, l))

