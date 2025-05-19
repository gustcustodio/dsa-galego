def binary_search(nums, n, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    while low < high:
        mid = int((low + high) / 2)

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            low = mid + 1
        else:
            high = mid
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr)
    rightPointer = 1

    while rightPointer < n and arr[rightPointer] < target:
        rightPointer *= 2

    if arr[rightPointer] == target:
        return 1

    return binary_search(arr, target, rightPointer//2, min(rightPointer, n - 1))


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
target = 32
result = exponential_search(array, target)

print(f"Element found at index {result}")
