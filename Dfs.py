# graph= {0:[1,2,3],1:[0,2],2:[0,1,3],3:[0,2]}
graph = {0:[1,2],1:[0,3],2:[0],3:[1]}

visited = [0]*4
res = []
def dfs(node):
    if visited[node] : 
        return 
    
    visited[node] = 1 
    res.append(node) 
    for i in graph[node] :
        if not visited[i] :
            dfs(i) 
    
dfs(0)