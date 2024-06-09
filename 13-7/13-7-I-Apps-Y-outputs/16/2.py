
def is_approved(numbers):
    for num in numbers:
        if num % 2 == 0 and not (num % 3 == 0 or num % 5 == 0):
            return "DENIED"
    return "APPROVED"

