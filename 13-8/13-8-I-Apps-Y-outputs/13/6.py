
def plus_one(digits):
    
    if digits == [0]:
        return [1]
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits

def main():
    print(plus_one([1,2,3]))
    print(plus_one([4,3,2,1]))

if __name__ == '__main__':
    main()

