from collections import defaultdict
def bfs(i):
  l=[]
  visited[i]=True
  l.append(i)
  while(len(l)):
    u=l[0]
    print(u,end=' ')
    l.pop(0)
    for v in graph[u]:
      if not visited[v]:
        visited[v]=True
        l.append(v)
  
def basebfs(v):
  for i in range(v):
    if not visited[i]:
      bfs(i)

if __name__=='__main__':
  v,e=map(int,input().split())
  graph=defaultdict(list)
  for i in range(e):
    v1,e1=map(int,input().split())
    graph[v1].append(e1)
    graph[e1].append(v1)
  visited=defaultdict(bool)
  basebfs(v)
