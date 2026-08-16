class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        
        unvisited, visiting, visited = 0, 1, 2
        states = [unvisited] * numCourses
        def dfs(i):
            if states[i] == visiting:
                return False
            elif states[i] == visited:
                return True
            states[i] = visiting
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            states[i] = visited
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return order