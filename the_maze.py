# The Maze
# https://leetcode.com/problems/the-maze/

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        visited = set()
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        
        def neighbors(row, col):
            temp = []
            used = set()
            used.add((row, col))
            
            for rowOffset, colOffset in directions:
                newRow = row
                newCol = col
                
                while 0 <= newRow + rowOffset < rows and 0 <= newCol + colOffset < cols and maze[newRow + rowOffset][newCol + colOffset] == 0:
                    newRow += rowOffset
                    newCol += colOffset
                
                if (newRow, newCol) not in used:
                    temp.append((newRow, newCol))
            
            return temp
        
        queue = collections.deque([(start[0], start[1])])
        
        while queue:
            cell = queue.popleft()
            
            if cell in visited:
                continue
            
            if cell == (destination[0], destination[1]):
                return True
            
            visited.add(cell)
            
            for neighbor in neighbors(cell[0], cell[1]):
                queue.append(neighbor)
        
        return False
