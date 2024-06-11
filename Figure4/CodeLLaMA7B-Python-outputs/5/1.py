from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(numbers[i])
            result.append(delimeter)
    return result


if __name__ == "