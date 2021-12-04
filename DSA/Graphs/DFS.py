from collections import defaultdict

def dfs(i):
  print(i,end=' ')
  visited[i]=True
  for u in graph[i]:
    if(not visited[u]):
      dfs(u)
def basedfs(v):
  for i in range(v):
    if(not visited[i]):
      dfs(i)

if __name__=='__main__':
  v,e=map(int,input().split())
  graph=defaultdict(list)
  for i in range(e):
    v1,e1=map(int,input().split())
    graph[v1].append(e1)
    graph[e1].append(v1)
  visited=defaultdict(bool)
  basedfs(v)
