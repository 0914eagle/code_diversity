from typing import List


def factorize(n: int) -> List[int]:
    
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    i = 3
    while n > 1:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 2
    return result


if __name__ == "__main__":
    print(factorize(int(input().strip())))
