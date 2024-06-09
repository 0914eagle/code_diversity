
import math

def expected_attempts(passwords):
    total_probability = sum(password[1] for password in passwords)
    expected_attempts = 0
    for password in passwords:
        expected_attempts += password[1] / total_probability * (math.log2(1 / password[1]) + 1)
    return expected_attempts

