def minPathSum(grid):
    # Get the number of rows and columns
    m, n = len(grid), len(grid[0])
    
    # Create a DP table to store the minimum path sum for each cell
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the top-left corner with the first element of the grid
    dp[0][0] = grid[0][0]
    
    # Initialize the first row (can only move right)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Initialize the first column (can only move down)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The answer is in the bottom-right corner
    return dp[m-1][n-1]

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

result = minPathSum(grid)
print("Minimum Path Sum:", result)
