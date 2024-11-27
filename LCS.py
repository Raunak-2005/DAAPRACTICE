def longest_common_subsequence(seq1, seq2):
    """Compute the longest common subsequence (LCS) between two sequences."""
    m, n = len(seq1), len(seq2)
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + seq1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    
    return dp[m][n]

a = "AABBAACJSAJHDHDBASJDBSHDA"
b = "ASHBDHIJSBDHYASBDHSABDASBHDBASDA"
print(longest_common_subsequence(a,b))