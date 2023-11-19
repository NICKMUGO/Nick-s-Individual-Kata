def find_unsorted_subarray(arr):
    n = len(arr)
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)) or all(arr[i] >= arr[i + 1] for i in range(n - 1)):
        return [0, 0]
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left:right + 1])
    while left > 0 and arr[left - 1] > min_val:
        left -= 1
    while right < n - 1 and arr[right + 1] < max_val:
        right += 1
    return [left, right]

arr = [1, 2, 3, 6, 4, 4]
result = find_unsorted_subarray(arr)
print(result)
