from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = deque()
        maxArea = 0

        for i in range(len(grid)):
            for x in range(len(grid[i])):
                if grid[i][x] == 1:
                    queue.append((i, x))
                    #visited
                    grid[i][x] = 0
                    area = 0
                    while len(queue) > 0:
                        curr = queue.popleft()
                        
                        area += 1

                        #up
                        if curr[0] > 0:
                            up = grid[curr[0]-1][curr[1]]
                            if up == 1:
                                queue.append((curr[0] - 1, curr[1]))
                                #visited
                                grid[curr[0] - 1][curr[1]] = 0
                        #down
                        if curr[0] < len(grid) - 1:
                            down = grid[curr[0]+1][curr[1]]
                            if down == 1:
                                queue.append((curr[0] + 1, curr[1]))
                                #visited
                                grid[curr[0] + 1][curr[1]] = 0
                        #left
                        if curr[1] > 0:
                            left = grid[curr[0]][curr[1] - 1]
                            if left == 1:
                                queue.append((curr[0], curr[1] - 1))
                                #visited
                                grid[curr[0]][curr[1] - 1] = 0
                        #right
                        if curr[1] < len(grid[0]) - 1:
                            right = grid[curr[0]][curr[1] + 1]
                            if right == 1:
                                queue.append((curr[0], curr[1] + 1))
                                #visited
                                grid[curr[0] ][curr[1] + 1] = 0
                    #compare area
                    maxArea = max(maxArea, area)
        
        return maxArea
                    