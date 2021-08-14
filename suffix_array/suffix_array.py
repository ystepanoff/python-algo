def suffix_array(s):
    n = len(s)
    p, c = [i for i in range(n)], [0] * n
    p = sorted(p, key=lambda i: s[i])
    for i in range(1, n):
        c[p[i]] = c[p[i - 1]]
        if s[p[i]] != s[p[i - 1]]:
            c[p[i]] += 1
    k = 0
    while (1 << k) < n:
        for i in range(n):
            p[i] = (p[i] - (1 << k) + n) % n
        cnt, pos = [0] * n, [0] * n
        for x in c:
            cnt[x] += 1
        for i in range(1, n):
            pos[i] = pos[i - 1] + cnt[i - 1]
        p_next = [0] * n
        for x in p:
            p_next[pos[c[x]]] = x
            pos[c[x]] += 1
        p = p_next
        c_next = [0] * n
        for i in range(1, n):
            prev = (c[p[i - 1]], c[(p[i - 1] + (1 << k)) % n])
            curr = (c[p[i]], c[(p[i] + (1 << k)) % n])
            c_next[p[i]] = c_next[p[i - 1]]
            if prev != curr:
                c_next[p[i]] += 1
        c = c_next
        k += 1
    return p, c


def lcp_array(s, p, c):
    n, k = len(p), 0
    lcp = [0] * n
    for i in range(n - 1):
        j = p[c[i] - 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[c[i]] = k
        k = max(k - 1, 0)
    return lcp


if __name__ == '__main__':
    s = input()
    s += '$'
    p, c = suffix_array(s)
    for x in p:
        print(x, end=' ')
    print()
    lcp = lcp_array(s, p, c)
    for i in range(1, len(lcp)):
        print(lcp[i], end=' ')
    print()
