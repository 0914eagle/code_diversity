
def get_tea_order(n, k, a, b):
    if n > a + b:
        return "NO"
    
    green_tea = "G" * a
    black_tea = "B" * b
    
    tea_order = []
    for i in range(n):
        if i % 2 == 0:
            tea_order.append(green_tea[i % a])
        else:
            tea_order.append(black_tea[i % b])
    
    return "".join(tea_order)

