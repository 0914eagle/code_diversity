
def check_error(message):
    if len(message) < 2:
        return "NO"
    
    for i in range(len(message) - 1):
        if message[i] == message[i+1]:
            return "YES\n" + message[i]
    
    return "NO"

