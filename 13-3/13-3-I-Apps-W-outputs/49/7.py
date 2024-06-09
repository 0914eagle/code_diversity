
def get_min_operations(operations):
    # Initialize a min heap and a counter for the number of operations
    heap = []
    count = 0
    
    # Iterate through the operations
    for operation in operations:
        # If the operation is "insert", add the number to the heap
        if operation[0] == "insert":
            heap.append(operation[1])
            count += 1
        # If the operation is "getMin", get the minimum number from the heap
        elif operation[0] == "getMin":
            # If the heap is empty, add a "removeMin" operation to make the heap non-empty
            if not heap:
                heap.append(operation[1])
                count += 1
            # Get the minimum number from the heap and compare it to the expected minimum
            actual_min = heap[0]
            expected_min = operation[1]
            # If the minimum numbers are not equal, add "removeMin" operations to make them equal
            while actual_min != expected_min:
                heap.append(expected_min)
                count += 1
                actual_min = heap[0]
    
    # Return the number of operations needed to make the sequence correct
    return count

