def mark_boundary_connected_zeros(matrix, x, y, visited):
    rows, cols = len(matrix), len(matrix[0])
    stack = [(x, y)]
    
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 0 and (nr, nc) not in visited:
                stack.append((nr, nc))

def replace_zeros(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    # Mark all boundary connected zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0 and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                mark_boundary_connected_zeros(matrix, i, j, visited)
    
    # Replace all non-boundary connected zeros with ones
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0 and (i, j) not in visited:
                matrix[i][j] = 1
                
    return matrix

# Input matrix
matrix = [
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
]

# Get the output matrix
output_matrix = replace_zeros(matrix)

# Print the output matrix
for row in output_matrix:
    print(row)
