
def immigration_officer(numbers):
    for num in numbers:
        if num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
            return "DENIED"
    return "APPROVED"

