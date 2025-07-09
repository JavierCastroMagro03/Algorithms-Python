import heapq as hq


def prim_pq(g):
    pq = []
    hq.heappush(pq, (0, 0, 0))  # coste, nodo_origen, nodo_destino
    visited = set()
    totalCost = 0
    while pq:  # while len(pq) > 0
        pair = hq.heappop(pq)
        c = pair[0]
        v = pair[1]
        if v not in visited:
            totalCost += c
            visited.add(v)

            for u in g[v]:
                if u[0] not in visited:
                    hq.heappush(pq, (u[1], u[0]))  # coste, nodo_origen, nodo_destino

    return totalCost


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        u, v, c = map(int, input().strip().split())
        g[u].append((v, c))
        g[v].append((u, c))
    cost = prim_pq(g)
    print(cost)

''' 
7 11
0 2 1
0 3 2
0 6 6
1 5 4
1 4 2
1 6 7
2 3 3
2 6 5
3 4 1
3 5 9
4 6 8
'''