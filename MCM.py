def sort_matrices_for_multiplication(matrices):
    """
    Sort matrices for valid multiplication order.
    Returns a list of matrices in the correct order.
    """
    sorted_matrices = [matrices[0]]
    used = [False] * len(matrices)
    used[0] = True

    for _ in range(len(matrices) - 1):
        for i in range(1, len(matrices)):
            if not used[i]:
                if sorted_matrices[-1][1] == matrices[i][0]:
                    sorted_matrices.append(matrices[i])
                    used[i] = True
                    break
                elif matrices[i][1] == sorted_matrices[0][0]:
                    sorted_matrices.insert(0, matrices[i])
                    used[i] = True
                    break

    return sorted_matrices


def matrix_chain_order(dimensions):
    """Calculate minimum number of multiplications needed for matrix chain."""
    n = len(dimensions) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m[0][n - 1] , s


def print_parenthesis(s, i , j):
    if i == j:
        return f"M{i}"
    else:
        k = s[i][j]
        left = print_parenthesis(s, i ,k)
        right = print_parenthesis(s , k+1 , j)
        return f"({left} x {right})"
