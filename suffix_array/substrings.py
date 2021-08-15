from functools import cmp_to_key

def preprocess(s):
    n = len(s)
    p, c_curr = [i for i in range(n)], [0] * n
    p = sorted(p, key=lambda i: s[i])
    for i in range(1, n):
        c_curr[p[i]] = c_curr[p[i - 1]]
        if s[p[i]] != s[p[i - 1]]:
            c_curr[p[i]] += 1
    c = [c_curr]
    k = 0
    while (1 << k) < n and c_curr[p[n - 1]] != n - 1:
        for i in range(n):
            p[i] = (p[i] - (1 << k) + n) % n
        cnt, pos, p_next = [0] * n, [0] * n, [0] * n
        for x in c_curr:
            cnt[x] += 1
        for i in range(1, n):
            pos[i] = pos[i - 1] + cnt[i - 1]
        for x in p:
            p_next[pos[c_curr[x]]] = x
            pos[c_curr[x]] += 1
        p = p_next
        c_next = [0] * n
        for i in range(1, n):
            prev = (c_curr[p[i - 1]], c_curr[(p[i - 1] + (1 << k)) % n])
            curr = (c_curr[p[i]], c_curr[(p[i] + (1 << k)) % n])
            c_next[p[i]] = c_next[p[i - 1]]
            if prev != curr:
                c_next[p[i]] += 1
        c_curr = c_next
        c.append(c_curr)
        k += 1
    return p, c


def compare(c, p1, p2):
    i1, j1 = p1
    i2, j2 = p2
    l1, l2 = j1 - i1 + 1, j2 - i2 + 1
    l = min(l1, l2)
    k = 0
    while (1 << k) <= l:
        k += 1
    k -= 1
    k = min(k, len(c) - 1)
    a = (c[k][i1 - 1], c[k][i1 + l - (1 << k) - 1])
    b = (c[k][i2 - 1], c[k][i2 + l - (1 << k) - 1])
    if a != b:
        return -1 if a < b else 1
    if l1 != l2:
        return -1 if l1 < l2 else 1
    return -1 if p1 < p2 else 1 if p1 > p2 else 0


if __name__ == '__main__':
    s = input()
    s += '$'
    p, c = preprocess(s)
    # Sort the set of m substrings given as pairs (l, r) lexicographically.
    # Substring comparison is performed in O(1) time. 
    m = int(input())
    pairs = []
    for i in range(m):
        l, r = map(int, input().split())
        pairs.append((l, r))
    pairs = sorted(pairs, key=cmp_to_key(lambda p1, p2: compare(c, p1, p2)))
    for l, r in pairs:
        print(l, r)
