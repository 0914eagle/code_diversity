
def simplify(x: str, n: str) -> bool:
    
    x_num, x_denom = x.split('/')
    n_num, n_denom = n.split('/')
    product = int(x_num) * int(n_num) // int(x_denom) * int(n_denom)
    return product % int(x_denom) == 0 and product % int(n_denom) == 0

