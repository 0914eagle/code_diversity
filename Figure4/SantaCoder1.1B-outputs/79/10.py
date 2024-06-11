def decimal_to_binary(decimal):
    
    binary_string = ""
    while decimal > 0:
        binary_string = str(decimal % 2) + binary_string
        decimal = decimal // 2
    return "db" + binary_string


