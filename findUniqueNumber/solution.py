def find_uniq(arr):
    if arr.count(max(arr)) > arr.count(min(arr)):
        return min(arr)
    else:
        return max(arr)