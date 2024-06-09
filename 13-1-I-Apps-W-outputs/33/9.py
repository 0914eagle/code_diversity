
def solve(w, h):
    # Calculate the number of possible tilings
    num_tilings = (w * h) * 4
    
    # Calculate the number of invalid tilings
    num_invalid_tilings = (w - 1) * (h - 1) * 2
    
    # Calculate the number of valid tilings
    num_valid_tilings = num_tilings - num_invalid_tilings
    
    # Calculate the remainder when divided by 998244353
    remainder = num_valid_tilings % 998244353
    
    return remainder

