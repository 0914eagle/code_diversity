
def get_tea_order(n, k, a, b):
    if n > a + b:
        return "NO"
    
    tea_order = []
    while len(tea_order) < n:
        if len(tea_order) - tea_order.count("G") < k:
            tea_order.append("G")
        else:
            tea_order.append("B")
    
    return "".join(tea_order)

