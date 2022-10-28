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
print("Breadth first order is")
vist={i:False for i in l}
q=[start]
while q:
    v=q[0]
    q.pop(0)
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

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')

'''
