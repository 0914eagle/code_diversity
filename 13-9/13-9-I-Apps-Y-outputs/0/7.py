
def withdraw_money(N):
    # Initialize variables
    operations = 0
    current_amount = 0

    # While the current amount is less than the target amount
    while current_amount < N:
        # If the current amount is less than 6, withdraw 1 yen
        if current_amount < 6:
            current_amount += 1
        # If the current amount is greater than or equal to 6 but less than 36, withdraw 6 yen
        elif current_amount < 36:
            current_amount += 6
        # If the current amount is greater than or equal to 36 but less than 81, withdraw 36 yen
        elif current_amount < 81:
            current_amount += 36
        # If the current amount is greater than or equal to 81 but less than 216, withdraw 81 yen
        elif current_amount < 216:
            current_amount += 81
        # If the current amount is greater than or equal to 216 but less than 729, withdraw 216 yen
        elif current_amount < 729:
            current_amount += 216
        # If the current amount is greater than or equal to 729 but less than 1681, withdraw 729 yen
        elif current_amount < 1681:
            current_amount += 729
        # If the current amount is greater than or equal to 1681 but less than 4032, withdraw 1681 yen
        elif current_amount < 4032:
            current_amount += 1681
        # If the current amount is greater than or equal to 4032 but less than 10000, withdraw 4032 yen
        elif current_amount < 10000:
            current_amount += 4032
        # If the current amount is greater than or equal to 10000 but less than 20000, withdraw 10000 yen
        elif current_amount < 20000:
            current_amount += 10000
        # If the current amount is greater than or equal to 20000 but less than 40000, withdraw 20000 yen
        elif current_amount < 40000:
            current_amount += 20000
        # If the current amount is greater than or equal to 40000 but less than 60000, withdraw 40000 yen
        elif current_amount < 60000:
            current_amount += 40000
        # If the current amount is greater than or equal to 60000 but less than 80000, withdraw 60000 yen
        elif current_amount < 80000:
            current_amount += 60000
        # If the current amount is greater than or equal to 80000 but less than 100000, withdraw 80000 yen
        elif current_amount < 100000:
            current_amount += 80000
        # If the current amount is greater than or equal to 100000, withdraw 100000 yen
        else:
            current_amount += 100000
        operations += 1

    return operations

