def decimal_to_binary(decimal):
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = int(decimal / 2)
    return "db" + binary


