"""
For an arr with len n, random select a value from arr [0, n-1] and get the idx.
Make the left part <= x, right part > x, put x in the last of left part.
Repeat the same process for left and right part.

Why random select a value:
- For random behavior, the time complexity should be the expectation, not the worst case.
- It is meaningless to always consider the worst case of a random behavior, because the worst
case is always infinite.

In the worst case of a quick sort, O(N^2) and O(N^2) (选到的x位于两侧)
In the best case of a quick sort, T(N) = 2 * T(N/2) + O(N) = O(NlogN) and O(logN)（选到的x靠近中心）

好处是我们随机选x。

x在任意一个位置的可能性是相等的。对于这样的x，算法的总体期望是O(N*logN) and O(logN)
"""

import random


def _randomized_quick_sort(l: int, r: int):

    if l >= r:
        return

    x: int = ARR[l + int(random.random() * (r - l + 1))]
    mid_l, mid_r = _partition(l, r, x)
    _randomized_quick_sort(l, mid_l - 1)
    _randomized_quick_sort(mid_r + 1, r)


def _partition(l: int, r: int, x: int) -> tuple[int, int]:
    i: int = l
    while i <= r:
        if ARR[i] < x:
            ARR[i], ARR[l] = ARR[l], ARR[i]
            l += 1
            i += 1
        elif ARR[i] == x:
            i += 1
        else:
            ARR[i], ARR[r] = ARR[r], ARR[i]
            r -= 1
    return l, r


ARR = [6, 5, 3, 4, 2, 1, 8, 7, 9, 0]
_randomized_quick_sort(0, len(ARR)-1)
print(ARR)
