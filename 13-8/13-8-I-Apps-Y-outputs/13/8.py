
def plus_one(digits):
    
    if digits == [0]:
        return [1]
    else:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                break
        return digits

def main():
    print(plus_one([1, 2, 3]))
    print(plus_one([4, 3, 2, 1]))

if __name__ == '__main__':
    main()

