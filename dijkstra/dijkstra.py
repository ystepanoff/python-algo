from heapq import heappush, heappop


inf = float('inf')


def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S:
            continue
        S.add(u)

        for v in G[u]:
            d = D.get(u, inf) + G[u][v]
            if d < D.get(v, inf):
                D[v], P[v] = d, u
            heappush(Q, (D[v], v))

    return D, P


if __name__ == '__main__':
    with open('input.txt', 'rt') as input:
        m, n, s, t = map(int, input.readline().split())
        s -= 1
        t -= 1

        G = [{} for j in range(m)]
        for i in range(n):
            a, b, w = map(int, input.readline().split())
            G[a-1][b-1] = w

    D, P = dijkstra(G, s)

    with open('output.txt', 'wt') as output:
        output.write('Shortest path from %d to %d has length %d.\n' % (s+1, t+1, D[t]))
        path = []
        while t != s:
            path.append(str(t+1))
            t = P[t]
        path.append(str(s+1))
        output.write(' --> '.join(reversed(path)))
        output.write('\n')
