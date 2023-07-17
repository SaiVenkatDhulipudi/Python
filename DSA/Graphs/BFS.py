from collections import defaultdict


def bfs(i):
    lis = []
    visited[i] = True
    lis.append(i)
    while len(lis):
        u = lis[0]
        print(u, end=" ")
        lis.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                lis.append(v)


def basebfs(v):
    for i in range(v):
        if not visited[i]:
            bfs(i)


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for i in range(e):
        v1, e1 = map(int, input().split())
        graph[v1].append(e1)
        graph[e1].append(v1)
    visited = defaultdict(bool)
    basebfs(v)
