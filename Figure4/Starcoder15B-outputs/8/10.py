from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_ = 0
    product = 1
    for number in numbers:
        sum_ += number
        product *= number
    return sum_, product


if __name__ == '__main__':
    import doctest

    doctest.testmod()
/tasks/task_1_2.