def subset_sum_approx(arr, target):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    current_sum = 0
    selected_elements = []
    
    # Iterate through the sorted array and add elements to the sum
    for num in arr:
        if current_sum + num <= target:
            selected_elements.append(num)
            current_sum += num
        
        # Stop if the current sum is equal to or greater than the target
        if current_sum == target:
            break
    
    return selected_elements, current_sum

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
target = 9
subset, sum_achieved = subset_sum_approx(arr, target)

print(f"Subset: {subset}")
print(f"Sum achieved: {sum_achieved}")
