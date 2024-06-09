
def solve(n, log):
    # Initialize variables
    heap = []
    result = []
    min_value = None

    # Iterate through the log
    for record in log:
        # Split the record into operation and value
        operation, value = record.split()

        # Insert operation
        if operation == "insert":
            heap.append(int(value))

        # Get minimum operation
        elif operation == "getMin":
            # If the heap is empty, add a removeMin operation to the result
            if not heap:
                result.append("removeMin")
            # If the heap is not empty, add a getMin operation to the result
            else:
                result.append(record)
                min_value = int(value)

        # Remove minimum operation
        elif operation == "removeMin":
            # If the heap is empty, do nothing
            if not heap:
                continue
            # If the heap is not empty, remove the minimum value from the heap
            else:
                removed_value = heap.pop(0)
                # If the removed value is not equal to the minimum value, add an insert operation to the result
                if removed_value != min_value:
                    result.append(f"insert {min_value}")

    # Return the result
    return result

