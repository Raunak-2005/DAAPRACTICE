def maxSumSubarray(arr):
    # Initialize prefix sum and minimum prefix sum
    n = len(arr)
    prefix_sum = [0] * (n + 1)  # Prefix sum array
    
    # Step 1: Calculate the prefix sum array
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    # Step 2: Find the maximum subarray sum using the prefix sum
    max_sum = float('-inf')  # Initialize to negative infinity
    min_prefix_sum = 0  # This keeps track of the minimum prefix sum seen so far
    
    for j in range(1, n + 1):
        # Calculate the sum of subarray arr[i...j-1] using prefix sums
        max_sum = max(max_sum, prefix_sum[j] - min_prefix_sum)
        # Update the minimum prefix sum
        min_prefix_sum = min(min_prefix_sum, prefix_sum[j])
    
    return max_sum

# Example usage:
arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
result = maxSumSubarray(arr)
print(f"Maximum sum subarray: {result}")
