import heapq
from collections import defaultdict

class Solution:
    def a_star(self, V, edges, src, dest, heuristic):
        adj = defaultdict(list)
        
        
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])  
        
        minheap = [[heuristic[src], 0, src]] 
        distances = [10**4] * V 
        distances[src] = 0
        
        while minheap:
            f, g, node = heapq.heappop(minheap)
            
            if node == dest:
                return g 
            
            for neighbor, weight in adj[node]:
                if distances[neighbor] > g + weight:
                    distances[neighbor] = g + weight
                    f_score = distances[neighbor] + heuristic[neighbor]
                    heapq.heappush(minheap, [f_score, distances[neighbor], neighbor])
        
        return -1  

if __name__ == "__main__":
    V = 5  
    
    edges = [
        [0, 1, 2],
        [0, 2, 4],
        [1, 2, 1],
        [1, 3, 7],
        [2, 4, 3],
        [3, 4, 1]
    ]
    
    src = 0  
    dest = 4  
    
    heuristic = [7, 6, 2, 1, 0]
    
    sol = Solution()
    ans = sol.a_star(V, edges, src, dest, heuristic)
    print(f"Shortest path cost from {src} to {dest} = {ans}")
