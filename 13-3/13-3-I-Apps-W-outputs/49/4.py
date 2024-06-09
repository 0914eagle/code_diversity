
def solve(n, log):
    # Initialize variables
    heap = []
    corrected_log = []
    min_value = 0
    remove_count = 0

    # Iterate through the log
    for record in log:
        # Get the operation and value
        operation, value = record.split()

        # Check if the operation is insert
        if operation == "insert":
            # Add the value to the heap
            heap.append(int(value))

        # Check if the operation is getMin
        elif operation == "getMin":
            # Get the minimum value in the heap
            min_value = min(heap)

            # Check if the minimum value is equal to the expected value
            if min_value != int(value):
                # Add the correct value to the corrected log
                corrected_log.append(f"insert {int(value) - min_value}")

                # Remove the minimum value from the heap
                heap.remove(min_value)

                # Increment the remove count
                remove_count += 1

        # Check if the operation is removeMin
        elif operation == "removeMin":
            # Get the minimum value in the heap
            min_value = min(heap)

            # Check if the minimum value is equal to the expected value
            if min_value != int(value):
                # Add the correct value to the corrected log
                corrected_log.append(f"insert {int(value) - min_value}")

                # Remove the minimum value from the heap
                heap.remove(min_value)

                # Increment the remove count
                remove_count += 1

    # Return the minimum number of records and the corrected log
    return remove_count, corrected_log

