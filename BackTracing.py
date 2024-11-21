grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]]


#  number of solutions
solution = 0


#  maximum values of x and y coordinates
maxX = len(grid[0])-1
maxY = len(grid)-1

#  endpoint coordinates, top(y=0) right(x=maxX) of the maze
endX = maxX
endY = 0

#  starting point coordinates, bottom(y=maxY) left(x=0) of the maze
mazeStartX = 0
mazeStartY = maxY

def number_of_paths(startX, startY):
    global solution
    global grid
    global mask
    
    
    #  if we reached the goal, return at this point
    if (startX == endX and startY == endY):
        solution += 1
        return
    
    
    #  possible directions are 
    #RIGHT (+1x, 0y)
    #UP (0x, -1y)
    #LEFT (-1x, 0y)
    #DOWN (0x, +1y)
    #  I use a direction array like this to avoid nested ifs inside the for loop
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
   
    for d in range(len(dx)):
        newX = startX + dx[d]
        newY = startY + dy[d]
        
        #  out of maze bounds
        if (newX < 0 or newY < 0):
            continue
        
        #  out of maze bounds
        if (newX > maxX or newY > maxY):
            continue
            
       
        if (grid[newY][newX] == 1):
            #  this are is already visited 
            continue
        else:
            #  branch from this point
            grid[newY][newX] = 1
            number_of_paths(newX, newY)
            grid[newY][newX] = 0


if __name__ == '__main__':
    number_of_paths(mazeStartX, mazeStartY)
    print(grid)
    print(solution)