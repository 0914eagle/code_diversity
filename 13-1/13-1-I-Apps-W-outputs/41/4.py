
def password_check(p, h):
    p_prime = ''.join(sorted(p))
    s1, s2, h_prime = h[:3], h[3:6], h[6:]
    return h_prime == p_prime + s1 + s2

