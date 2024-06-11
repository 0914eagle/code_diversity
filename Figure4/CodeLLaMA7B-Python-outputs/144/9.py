def simplify(x, n):
    
    num1, den1 = x.split("/")
    num2, den2 = n.split("/")
    num1, den1 = int(num1), int(den1)
    num2, den2 = int(num2), int(den2)
    if num1 * den2 == num2 * den1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "1