
def solve(n, a, f):
    # Initialize the maximum number to be the original number
    max_num = int(a)
    # Iterate over each possible segment length
    for seg_len in range(1, n + 1):
        # Iterate over each possible starting index for the segment
        for start_idx in range(n - seg_len + 1):
            # Extract the segment from the original number
            segment = int(a[start_idx:start_idx + seg_len])
            # Apply the function to the segment
            transformed_segment = int(str(segment).translate(str.maketrans("123456789", "".join(map(str, f)))))
            # Calculate the maximum number obtained by replacing the segment with the transformed segment
            max_num = max(max_num, int(a[:start_idx] + str(transformed_segment) + a[start_idx + seg_len:]))
    return max_num

