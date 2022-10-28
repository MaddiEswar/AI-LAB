# program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    # store minimum weight
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
    # store current Path weight(cost)
        current_pathweight = 0
    # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
     # update minimum
        min_path = min(min_path, current_pathweight)
    return min_path
# Driver Code
if __name__ == "__main__":
 # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))



    
'''
def solve(v,c,d,dis):
    if v==x and c==n:
        return dis[v]
    ans=float('inf')
    for i in l[v]:
        u,w=i
        if u==x and c!=n-1:
            continue
        if u not in d:
            d[u]=v
            dis[u]=w+dis[v]
            ans=min(ans,solve(u,c+1,d,dis))
            del d[u]
    return ans

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))
l={i:[] for i in range(1,n+1)}
print("Enter edges (source, destination, weight)")
for i in range(m):
    u, v, w = map(int, input().split())
    l[u].append([v,w])
x = int(input("Enter starting node: "))
dis={x:0}
d={}
print("Shortest distance:",solve(x,0,d,dis))
'''


'''

Sample input:-

1 2 10
2 1 5
1 3 15
3 1 6
1 4 20
4 1 8
2 4 10
4 2 8
2 3 9
3 2 13
3 4 12
4 3 9

'''
