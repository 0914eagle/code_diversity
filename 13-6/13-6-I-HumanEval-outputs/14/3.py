
def digitSum(s: str) -> int:
    
    upper_case_ascii_codes = [ord(char) for char in s if char.isupper()]
    return sum(upper_case_ascii_codes)

