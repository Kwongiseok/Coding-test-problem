import sys
sys.setrecursionlimit(10000)
#sys.stdin = open('test.txt','rt')

def kruskal(graph,M) :
    cnt = 0
    merge = []
    for i in range(M) :
        root1 = getparent(graph[i][0])
        root2 = getparent(graph[i][1])
        if root1 != root2 :
            #print(getparent(graph[i][0]), getparent(graph[i][1]))
            if rank[root1] > rank[root2] :
                parent[root2] = root1
            else :
                parent[root1] = root2
                if rank[root1] == rank[root2] :
                    rank[root2]+=1


            merge.append(graph[i])
    merge.sort(key = lambda merge : merge[2])
    merge.pop()
    for i in range(len(merge)) :
        cnt+=merge[i][2]
    return cnt
def getparent(node) :
    if parent[node] != node :
        parent[node] = getparent(parent[node])
    return parent[node]

N , M = map(int,sys.stdin.readline().split())

graph = []
for i in range(M) :
    A,B,C = map(int,sys.stdin.readline().split())
    graph.append([A,B,C])

graph.sort(key = lambda graph : graph[2])

parent = [ i for i in range(N+1) ]
rank = [ 0 for i in range(N+1)]
length = kruskal(graph,M)
print(length)
