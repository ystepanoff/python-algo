# RSQ implementation using a Segment Tree

import numpy as np


class SegmentTree:
    def __init__(self, N, a=None):
        self.N = N
        self.ST = np.zeros(N << 1).astype('int')
        
        if a:
            for i, v in enumerate(a):
                self.ST[n + i] = v;
                
            for i in range(self.N - 1, 0, -1):
                self.ST[i] = self.ST[i << 1] + self.ST[i << 1 | 1];
                
    def set_value(self, i, value):
        i += self.N
        
        while i > 1:
            self.ST[i >> 1] = self.ST[i] + self.ST[i ^ 1]
            i >>= 1

    def sum(self, l, r):
        result = 0
        l += self.N
        r += self.N
        
        while l < r:
            if l & 1:
                result += self.ST[l]
                l += 1
            if r & 1:
                r -= 1
                result += self.ST[r]
                
            l >>= 1
            r >>= 1
                
        return result
        
        
if __name__ == '__main__':
    with open('input.txt', 'rt') as input:
        n, m = map(int, input.readline().split())
        a = map(int, input.readline().split())

        t = SegmentTree(n, a)

        with open('output.txt', 'wt') as output:
            for i in range(m):
                l, r = map(int, input.readline().split())
                output.write('Sum on the subrange [%d..%d] is %d.\n' % (l, r, t.sum(l - 1, r)))