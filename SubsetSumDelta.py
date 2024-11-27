def delta_approx_subset_sum(arr, target, delta):
    # Initialize a DP array to track possible sums up to target
    max_sum = int(target / delta) + 1  # Approximate maximum sum divided by delta
    dp = [False] * (max_sum + 1)  # DP table, to track which sums are possible
    dp[0] = True  # Sum of 0 is always achievable
    
    # Process each number in the array
    for num in arr:
        # Traverse the DP table in reverse to avoid re-using the same element
        for j in range(max_sum, -1, -1):
            if dp[j]:
                new_sum = j + int(num / delta)
                if new_sum <= max_sum:
                    dp[new_sum] = True
    
    # Find the largest sum that is less than or equal to the target and is a multiple of delta
    closest_sum = -1
    for i in range(int(target / delta), -1, -1):
        if dp[i]:
            closest_sum = i * delta
            break
    
    return closest_sum

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
target = 9
delta = 1  # Set delta to the desired approximation factor
approx_sum = delta_approx_subset_sum(arr, target, delta)

print(f"Approximate subset sum: {approx_sum}")
