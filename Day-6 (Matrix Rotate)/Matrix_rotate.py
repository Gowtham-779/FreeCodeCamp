def rotate(matrix):
    r = len(matrix)
    c = len(matrix[0])
    result = []
    for i in range(c):
        new = []
        for j in range(r-1,-1,-1):
            new.append(matrix[j][i])
        result.append(new)
    return result