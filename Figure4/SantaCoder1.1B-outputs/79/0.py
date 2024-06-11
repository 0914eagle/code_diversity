def decimal_to_binary(decimal):
    
    binary_str = ""
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal = decimal // 2
    return "db" + binary_str


