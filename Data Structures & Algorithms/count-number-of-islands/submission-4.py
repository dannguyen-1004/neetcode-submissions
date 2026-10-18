class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        myDict = {}


        def spreadIsland(x: int, y: int):

            if y+1 < len(grid[0]) and grid[x][y + 1] == "1" and (x, y+1) not in myDict:
                myDict[(x, y+1)] = 1
                spreadIsland(x, y+1)
            if y - 1 >= 0 and grid[x][ y - 1] == "1" and (x, y-1) not in myDict:
                myDict[(x, y-1)] = 1
                spreadIsland(x, y-1)    
            
            if x+1 < len(grid) and grid[x+ 1][ y] == "1" and (x + 1, y) not in myDict:
                myDict[(x + 1, y)] = 1
                spreadIsland(x + 1, y)
            if x - 1 >= 0 and grid[x - 1][ y] == "1" and (x -1, y) not in myDict:
                myDict[(x -1, y)] = 1
                spreadIsland(x -1 , y)  
            
            return
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1" and (x, y) not in myDict:
                    count += 1
                    spreadIsland(x, y)
        
        
        return count
