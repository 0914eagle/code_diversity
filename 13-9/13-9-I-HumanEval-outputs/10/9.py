
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:
        return False
    else:
        sum_of_even_numbers = 0
        for i in range(1, int(n/2)+1):
            if i % 2 == 0:
                sum_of_even_numbers += i
        if sum_of_even_numbers == n:
            return True
        else:
            return False

