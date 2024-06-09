
def decrypt_message(encrypted_message, key):
    # Step 1: Define the function f(x) = (33x + 1) mod 2^20
    def f(x):
        return (33 * x + 1) % (2**20)
    
    # Step 2: Create a X by X size grid, fill the upper left corner with f^1(0), the next cell to the right with f^2(0), f^3(0) etc.
    grid = [[f(0) for _ in range(X)] for _ in range(X)]
    
    # Step 3: Sum all the values in every column, and take those values mod 2^20
    column_sums = [sum(column) % (2**20) for column in zip(*grid)]
    
    # Step 4: Concatenate the base-10 representations of the column sums together, to get a very long base-10 number
    long_number = int(''.join(str(sum) for sum in column_sums))
    
    # Step 5: Convert the result of step 4 from base 10 to base 27
    base_27_key = long_number % (27**X)
    
    # Step 6: For each letter l of the intercepted message, shift the letter by the amount given by the corresponding digit of step 5, base 27
    decrypted_message = ''
    for i, letter in enumerate(encrypted_message):
        decrypted_message += chr((ord(letter) + base_27_key[i]) % 27)
    
    return decrypted_message

