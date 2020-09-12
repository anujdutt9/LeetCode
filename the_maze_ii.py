# The Maze II

import sys
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        start, destination = tuple(start), tuple(destination)
        
        # Directions to Visit
        directions = [[-1,0], [0,1], [0,-1], [1,0]]
        
        # Function to get Adjacent Nodes
        def neighbors(maze, node):
            temp = []
            used = set()
            used.add(node)
            
            for rowOffset, colOffset in directions:
                (newRow, newCol) = node
                distance = 0
                
                while 0 <= newRow + rowOffset < rows and 0 <= newCol + colOffset < cols and maze[newRow + rowOffset][newCol + colOffset] == 0:
                    newRow += rowOffset
                    newCol += colOffset
                    distance += 1
                
                if (newRow, newCol) not in used:
                    temp.append((distance, (newRow, newCol)))
            return temp
        
        # Using the Heap
        # Root node has the minimum value
        heap = [(0, start)]
        
        visited = set()
        
        while heap:
            distance, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            if node == destination:
                return distance
            
            for neighbor_dist, neighbor in neighbors(maze, node):
                heapq.heappush(heap, (distance + neighbor_dist, neighbor))
        
        return -1
