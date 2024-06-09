
def f1(a, b, s):
    if a <= b:
        return "NO"
    
    if s.count(".") < a:
        return "NO"
    
    if s.count("X") + b >= a:
        return "NO"
    
    return "YES"

