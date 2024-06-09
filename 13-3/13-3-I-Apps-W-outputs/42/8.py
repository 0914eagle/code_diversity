
def get_tea_order(n, k, a, b):
    if n > a + b:
        return "NO"
    
    tea_order = []
    for i in range(n):
        if i % 2 == 0:
            tea_order.append("G")
        else:
            tea_order.append("B")
    
    return "".join(tea_order)

