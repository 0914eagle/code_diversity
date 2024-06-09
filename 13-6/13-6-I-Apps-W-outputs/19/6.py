
def get_maximum_fruits(lemons, apples, pears):
    # Find the greatest common divisor of lemons, apples, and pears
    gcd = _get_gcd(lemons, apples, pears)
    
    # Divide lemons, apples, and pears by their greatest common divisor
    # to get the maximum number of fruits that can be used in the compote
    max_lemons = lemons // gcd
    max_apples = apples // gcd
    max_pears = pears // gcd
    
    return max_lemons + max_apples + max_pears

def _get_gcd(a, b, c):
    if b == 0:
        return a
    else:
        return _get_gcd(b, c % b, a)

if __name__ == '__main__':
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    print(get_maximum_fruits(lemons, apples, pears))

