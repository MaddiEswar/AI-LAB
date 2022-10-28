n=int(input("Enter number of vertices: "))
m=int(input("Enter number of edges: "))
l={}
print("Enter edges (source, destination)")
for i in range(m):
    u,v=map(int,input().split())
    if u in l:
        l[u].append(v)
    else:
        l[u]=[v]
    if v in l:
        l[v].append(u)
    else:
        l[v]=[u]
start=int(input("Enter starting node: "))
print("Depth first order is")
vist={i:False for i in l}
q=[start]
while q:
    v=q[-1]
    q.pop()
    if vist[v]:
        continue
    vist[v]=True
    print(v)
    for i in l[v]:
        q.append(i)


'''
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = set() 
def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
'''
