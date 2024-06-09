
def decrypt(encrypted_text, N, X):
    # Step 1: Define the function f(x) = (33x + 1) mod 2^20
    def f(x):
        return (33*x + 1) % (2**20)
    
    # Step 2: Create a X by X size grid, fill the upper left corner with f^1(0), the next cell to the right with f^2(0), f^3(0) etc.
    grid = [[0] * X for _ in range(X)]
    grid[0][0] = f(0)
    for i in range(1, X):
        for j in range(i):
            grid[i][j] = f(grid[i-1][j])
    
    # Step 3: Sum all the values in every column, and take those values mod 2^20
    column_sums = [0] * X
    for i in range(X):
        for j in range(X):
            column_sums[i] += grid[j][i]
        column_sums[i] %= 2**20
    
    # Step 4: Concatenate the base-10 representations of the column sums together, to get a very long base-10 number
    base_10_number = ""
    for i in range(X):
        base_10_number += str(column_sums[i])
    
    # Step 5: Convert the result of step 4 from base 10 to base 27
    base_27_number = int(base_10_number, 10)
    
    # Step 6: For each letter l of the intercepted message, shift the letter by the amount given by the corresponding digit of step 5, base 27
    decrypted_text = ""
    for i in range(N):
        letter = encrypted_text[i]
        if letter == " ":
            decrypted_text += " "
        else:
            letter_value = ord(letter) - ord("A")
            shift_amount = base_27_number // (27**(N-i-1)) % 27
            decrypted_letter_value = (letter_value + shift_amount) % 27
            decrypted_text += chr(ord("A") + decrypted_letter_value)
    
    return decrypted_text

