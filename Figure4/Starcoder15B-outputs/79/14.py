def decimal_to_binary(decimal):
    
    binary = bin(decimal)
    return 'db' + binary[2:] + 'db'


