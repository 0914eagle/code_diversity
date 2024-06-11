def solve(N):
    
    # your code here
    # convert to binary
    binary = bin(N)
    # split into list of digits
    binary_list = list(binary)
    # remove '0b'
    binary_list = binary_list[2:]
    # convert to int
    binary_list = [int(i) for i in binary_list]
    # sum the digits
    binary_sum = sum(binary_list)
    # convert to binary
    binary_sum_binary = bin(binary_sum)
    # remove '0b'
    binary_sum_binary = binary_sum_binary[2:]
    # return the binary sum
    return binary_sum_binary


#