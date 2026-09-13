def find_missing_numbers(arr):
    missing = []
    n = max(arr)
    for i in range(1,n+1):
        if i not in arr:
            missing.append(i)
    return missing