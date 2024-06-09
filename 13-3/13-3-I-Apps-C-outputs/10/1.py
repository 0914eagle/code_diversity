
def f1(h, m, s, t_1, t_2):
    # Convert the input times to integers
    h1 = int(h) * 3600 + int(m) * 60 + int(s)
    h2 = int(t_1) * 3600 + int(t_2) * 60
    
    # Check if the target time is reachable
    if h2 > h1:
        return "YES"
    else:
        return "NO"

