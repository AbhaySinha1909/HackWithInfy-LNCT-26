class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        if destination in adj_list[source]:
            return True
        
        seen = set()
        seen.add(source)
        stk = [source]

        while stk:
            node = stk.pop()
            for nei_node in adj_list[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stk.append(nei_node)
        
        if destination in seen:
            return True
        else:
            return False