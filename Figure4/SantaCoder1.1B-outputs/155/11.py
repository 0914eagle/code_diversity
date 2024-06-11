def even_odd_count(num):
    
    return (sum(int(digit) for digit in str(num)),
            sum(int(digit) for digit in str(num) if digit % 2 == 0))


