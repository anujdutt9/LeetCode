# Course Schedule II

class Solution:
    white = 1
    gray = 2
    black = 3
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Create Adjacency List
        adjacency_list = defaultdict(list)
        
        # Add a pair of source -> dest in list
        for dest, src in prerequisites:
            adjacency_list[src].append(dest)
        
        # Stack
        stack = []
        is_possible = True
        
        # By default, all vertices are white
        color = {k: Solution.white for k in range(numCourses)}
        
        # Depth First Search
        def dfs(node):
            nonlocal is_possible
            
            # If cycle found, return
            if not is_possible:
                return
            
            # Start Recursion using DFS
            # The node which is being considered changes from white to gray
            color[node] = Solution.gray
            
            # For all nodes in adjacency list
            if node in adjacency_list:
                # Check for all neighbors to the node
                for neighbor in adjacency_list[node]:
                    # If the neighbor is unvisited, visit them
                    if color[neighbor] == Solution.white:
                        dfs(neighbor)
                    # else there exists a cycle
                    elif color[neighbor] == Solution.gray:
                        is_possible = False
            
            # Once dfs is done, mark the visited nodes as black
            color[node] = Solution.black
            
            # Append Node to Stack
            stack.append(node)
        
        
        # For vertices in numCourses, perform DFS
        for vertex in range(numCourses):
            # If node is unprocessed, perform dfs on it
            if color[vertex] == Solution.white:
                dfs(vertex)
        
        # Return all elements from the stack from top to bottom order, if no cycle found
        return stack[::-1] if is_possible else []
