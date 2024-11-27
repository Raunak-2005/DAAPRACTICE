def knapsack_approx(values, weights, W, epsilon):
    n = len(values)
    max_value = max(values)

    # Scaling factor
    K = (epsilon * max_value) / n

    # Scale the values
    scaled_values = [int(v / K) for v in values]

    # Initialize DP table
    dp = [0] * (W + 1)

    # Compute DP table
    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + scaled_values[i])

    # Find the maximum value and reconstruct the solution
    max_scaled_value = max(dp)
    result_weight = dp.index(max_scaled_value)

    # Backtrack to find the items included
    included_items = []
    remaining_weight = result_weight
    for i in range(n - 1, -1, -1):
        if remaining_weight >= weights[i] and dp[remaining_weight] == dp[remaining_weight - weights[i]] + scaled_values[i]:
            included_items.append(i)
            remaining_weight -= weights[i]

    # Return the original (unscaled) values for the result
    result_value = sum(values[i] for i in included_items)
    return result_value, included_items

# Example Usage
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]   # Weights of the items
W = 50                   # Capacity of the knapsack
epsilon = 0.1            # Accuracy parameter

result_value, included_items = knapsack_approx(values, weights, W, epsilon)
print(f"Approximate Maximum Value: {result_value}")
print(f"Included Items: {included_items}")
