def getSkyline(buildings):
    # Generate events
    events = []
    for left, right, height in buildings:
        events.append((left, height))   # Start event
        events.append((right, -height)) # End event

    # Sort events by x-coordinate, then height
    events.sort(key=lambda x: (x[0], -x[1] if x[1] > 0 else x[1]))

    # Result list and active heights list
    result = []
    heights = [0]  # Start with ground level
    prev_max_height = 0

    # Process events
    for x, h in events:
        if h > 0:  # Start of a building
            heights.append(h)
            heights.sort()  # Keep heights sorted
        else:  # End of a building
            heights.remove(-h)

        # Current maximum height
        curr_max_height = heights[-1]  # Last element is the tallest height

        # If the height changes, record the key point
        if curr_max_height != prev_max_height:
            result.append([x, curr_max_height])
            prev_max_height = curr_max_height

    return result

# Example usage
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(getSkyline(buildings))
