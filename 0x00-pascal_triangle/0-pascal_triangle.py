def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Start each row with 1s
        for j in range(1, i):
            # Each triangle value is the sum of the two values above it
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle

