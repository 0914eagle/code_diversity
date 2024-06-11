from typing import List


def factorize(n: int) -> List[int]:
    
    result = []
    i = 2
    while n > 1:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
    return result


if __name__ == "__main__":
    print("Example:")
    print(factorize(100))

    # These "asserts" are used