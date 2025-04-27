# graph= {0:[1,2,3],1:[0,2],2:[0,1,3],3:[0,2]}
graph = {0:[1,2],1:[0,3],2:[0],3:[1]}

queue = []
visited = [0] * 4
res = []
def bfs():
    while queue :
        curr_node = queue.pop(0) 
        res.append(curr_node)
        visited[curr_node] = 1 
        for i in graph[curr_node] :
            if not visited[i] :
                queue.append(i) 
                

queue.append(0)   
bfs()
print(res)