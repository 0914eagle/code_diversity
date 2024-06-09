
def sort_phone_numbers(numbers):
    
    return "\n".join(["+91 " + num[1:] if num.startswith("91") or num.startswith("0") else num for num in sorted(numbers)])

