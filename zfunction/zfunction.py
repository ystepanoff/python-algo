# Substring search in O(n + m) using Z-function.

def Z(s):
    n, l, r = len(s), 0, 0
    z = [0] * n
    for i in range(1, n):
        if r >= i:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n:
            if s[i + z[i]] != s[z[i]]:
                break
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

if __name__ == '__main__':
    with open('input.txt', 'rt') as input:
        s = input.readline().strip()
        p = input.readline().strip()
        n, m = len(s), len(p)
    with open('output.txt', 'wt') as output:
        t = p + '$' + s
        z = Z(t)
        for i in range(m, n + m + 1):
            if z[i] == m:
                output.write('pattern found at position {}\n'.format(i - m))
