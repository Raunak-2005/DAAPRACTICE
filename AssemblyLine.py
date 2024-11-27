def assembly_line_scheduling_n_lines(a, t, e, x):
    """
    Solve the assembly line scheduling problem for n lines using dynamic programming.

    Parameters:
        a (list of lists): Processing times at each station for n lines.
        t (3D list): Transfer times between lines at stations (t[k][i][j]).
        e (list): Entry times for n lines.
        x (list): Exit times for n lines.

    Returns:
        int: Minimum time to process through the assembly lines.
    """
    num_lines = len(a)  # Number of lines
    num_stations = len(a[0])  # Number of stations

    # Initialize a 2D array to store the minimum times for each line
    f = [[0] * num_stations for _ in range(num_lines)]

    # Initialize the times for the first station on all lines
    for i in range(num_lines):
        f[i][0] = e[i] + a[i][0]

    # Fill the DP table for the remaining stations
    for j in range(1, num_stations):  # Iterate over stations
        for i in range(num_lines):    # Iterate over lines
            # Start with the cost of staying on the same line
            f[i][j] = f[i][j - 1] + a[i][j]

            # Check transitions from all other lines
            for k in range(num_lines):  # Transition from line k to line i
                if k != i:
                    f[i][j] = min(f[i][j], f[k][j - 1] + t[k][i][j] + a[i][j])

    # Add the exit times to get the final costs for all lines
    final_times = [f[i][-1] + x[i] for i in range(num_lines)]

    # Return the minimum of the final times
    return min(final_times)


# Example usage:
a = [
    [4, 5, 3, 2],  # Line 1
    [2, 10, 1, 4],  # Line 2
    [6, 2, 9, 3]    # Line 3
]  # Processing times
t = [
    [[0, 7, 4, 5], [0, 8, 6, 4], [0, 3, 5, 2]],  # Line 1 to others
    [[0, 6, 3, 7], [0, 9, 2, 8], [0, 4, 6, 3]],  # Line 2 to others
    [[0, 5, 2, 3], [0, 4, 5, 6], [0, 3, 6, 1]]   # Line 3 to others
]  # Transfer times (t[k][i][j])
e = [10, 12, 15]  # Entry times for each line
x = [18, 7, 9]    # Exit times for each line

min_time = assembly_line_scheduling_n_lines(a, t, e, x)
print(f"Minimum time to process: {min_time}")
