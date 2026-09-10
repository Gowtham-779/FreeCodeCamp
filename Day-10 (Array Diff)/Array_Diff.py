def array_diff(arr1, arr2):
    result = []
    for i in arr1:
        if i not in arr2:
            result.append(i)
    for i in arr2:
        if  i not in arr1:
            result.append(i)
    result.sort()
    return result