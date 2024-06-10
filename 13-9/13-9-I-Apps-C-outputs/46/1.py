
def calculate_expected_payment(salaries):
    # Calculate the expected payment for each worker
    expected_payments = []
    for i in range(len(salaries)):
        expected_payment = 0
        for j in range(len(salaries)):
            if i != j and salaries[i] < salaries[j]:
                expected_payment += salaries[j] - salaries[i]
        expected_payments.append(expected_payment)
    
    # Calculate the total expected payment
    total_expected_payment = sum(expected_payments)
    
    # Return the total expected payment divided by the number of workers squared
    return total_expected_payment / (len(salaries) ** 2)

def main():
    # Read the number of workers and their salary ranges
    num_workers = int(input())
    salaries = []
    for i in range(num_workers):
        salary_range = input().split()
        salaries.append(float(salary_range[0]))
        salaries.append(float(salary_range[1]))
    
    # Calculate the expected payment and output the result
    expected_payment = calculate_expected_payment(salaries)
    print(expected_payment)

if __name__ == '__main__':
    main()

