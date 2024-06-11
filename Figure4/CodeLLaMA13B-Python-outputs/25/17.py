from typing import List


def factorize(n: int) -> List[int]:
    
    result = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result.append(i)
                n = n // i
                break
    return result


if __name__ == "__main__":
    print(factorize(8))
    print(factorize(25))
    print(factorize(7