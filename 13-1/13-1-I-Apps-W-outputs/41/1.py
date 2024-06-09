
def password_check(p, h):
    p_prime = ''.join(sorted(p))
    s1, s2, hash = h[:3], h[3:6], h[6:]
    return hash == s1 + p_prime + s2

