from typing import List


def factorize(n: int) -> List[int]:
    
    result = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                result.append(i)
                break
    return result


if __name__ == "__main__":
    print("Example:")
    print(factorize(100))

    # These "asserts"