def find_landing_spot(matrix):
    best = None
    lowest = float("+inf")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                danger = 0
                if i > 0:
                    danger += matrix[i-1][j]
                if i < len(matrix) - 1:
                    danger += matrix[i+1][j]
                if j > 0:
                    danger += matrix[i][j-1]
                if j < len(matrix[i]) - 1:
                    danger += matrix[i][j+1]
                if danger < lowest:
                    lowest = danger
                    best = [i,j]
    return best