class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            
            states[node] = visiting

            for nei_node in adj[node]:
                if not dfs(nei_node):
                    return False
            
            states[node] = visited

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True