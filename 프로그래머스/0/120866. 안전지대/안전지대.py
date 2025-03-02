def solution(board):
    n = len(board)
    danger_zone = set()

    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),  (0, 0),  (0, 1),  
                  (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n: 
                        danger_zone.add((ni, nj))

    total_cells = n * n
    return total_cells - len(danger_zone)
