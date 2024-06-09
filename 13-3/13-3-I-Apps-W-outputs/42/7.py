
def get_tea_order(n, k, a, b):
    if n > a + b:
        return "NO"
    
    tea_order = []
    while len(tea_order) < n:
        if len(tea_order) < a:
            tea_order.append("G")
        elif len(tea_order) < a + b:
            tea_order.append("B")
        else:
            if tea_order[-1] == tea_order[-k]:
                return "NO"
            if tea_order[-1] == "G":
                tea_order.append("B")
            else:
                tea_order.append("G")
    
    return "".join(tea_order)

