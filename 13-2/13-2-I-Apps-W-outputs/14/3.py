
def f1(s, a, b):
    if len(s) < a or len(s) < b:
        return "NO"
    
    if s.count(".") < a or s.count(".") < b:
        return "NO"
    
    if s.count("X") > 0:
        return "NO"
    
    return "YES"

