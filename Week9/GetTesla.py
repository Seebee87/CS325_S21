def getTesla(maze):
    col = len(maze[0])-1
    row = len(maze)-1
    empty = [["" for p in range(col+1)] for s in range(row+1)]
    empty[row][col] = maze[row][col]
    for i in reversed(range(row+1)):
        for j in reversed(range(col+1)):
            if j > 0: #we go left
                if empty[i][j-1] == "":
                    empty[i][j-1] = maze[i][j-1]+empty[i][j]
                else: 
                    empty[i][j-1] = max(empty[i][j-1], maze[i][j-1]+empty[i][j])
            if i > 0: #then we go up
                empty[i-1][j] = maze[i-1][j]+empty[i][j]
    keys = empty[0][0]
    if keys <=0:
        keys = abs(keys)
        return keys + 1
    else:
        return 1
        
