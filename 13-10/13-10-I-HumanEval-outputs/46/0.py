
def is_happy(s: str) -> bool:
    
    if len(s) < 3:
        return False
    
    window_size = 3
    window = s[:window_size]
    for i in range(len(s) - window_size + 1):
        if len(set(window)) != window_size:
            return False
        window = window[1:] + s[i + window_size - 1]
    return True

