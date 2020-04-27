import sys

#from collections import deque

sys.setrecursionlimit(10000)

#sys.stdin = open("test.txt","rt")

N,M = map(int,sys.stdin.readline().split())

def dfs(i) :

  visited[i] = True

  for j in adj[i] :

  if not visited[j] :

    dfs(j)

adj = [[] for _ in range(N+1)]

visited = [False]*(N+1)


for i in range(M) :

  x,y = map(int,sys.stdin.readline().split())

  adj[x].append(y)

  adj[y].append(x)



cnt = 0



for i in range(1,N+1) :

  if not visited[i] :

    dfs(i)

    cnt+=1


print(cnt)
