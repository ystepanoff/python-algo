# RSQ implementation using a Fenwick Tree


import numpy as np


class FenwickTree:
    def __init__(self, N):
        self.N = N
        self.FT = np.zeros(N + 1).astype('int')

    def increment(self, i, delta):
        while i <= self.N:
            self.FT[i] += delta
            i += i & -i

    def sum(self, l, r=None):
        if r:
            return self.sum(r) - self.sum(l - 1)

        result = 0
        while l > 0:
            result += self.FT[l]
            l -= l & -l

        return result


if __name__ == '__main__':
    with open('input.txt', 'rt') as input:
        n, m = map(int, input.readline().split())
        a = map(int, input.readline().split())

        t = FenwickTree(n)
        for i, v in enumerate(a):
            t.increment(i + 1, v)

        with open('output.txt', 'wt') as output:
            for i in range(m):
                l, r = map(int, input.readline().split())
                output.write('Sum on the subrange [%d..%d] is %d.\n' % (l, r, t.sum(l, r)))
