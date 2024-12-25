"""
Find the K th largest number in a unsorted list.

Only need the value, i don't need the idx.
If i can find the k th largest number, then i can find the N-K th smallest number.

You need to reach a time complexity of O(N)

Which means you cannot sort, the best time complexity of a sort will be O(N*logN)

O(N) and O(1)
"""

import random

def get_k_th_largest(l: int, r: int, k: int) -> int:

    x: int = ARR[l + int(random.random() * (r - l + 1))]
    mid_left: int
    mid_right: int
    mid_left, mid_right = _partition(l, r, x)

    if (k >= mid_left) and (k <= mid_right):
        return ARR[mid_left]
    elif (k < mid_left):
        return get_k_th_largest(l, mid_left - 1, k)
    elif (k > mid_right):
        return get_k_th_largest(mid_right + 1, r, k)
    else:
        raise Exception


def _partition(l: int, r: int, x: int) -> tuple[int, int]:
    i: int = l

    while i <= r:
        if ARR[i] < x:
            ARR[l], ARR[i] = ARR[i], ARR[l]
            i += 1
            l += 1

        elif ARR[i] == x:
            i += 1

        elif ARR[i] > x:
            ARR[r], ARR[i] = ARR[i], ARR[r]
            r -= 1

    return l, r


ARR = [random.randint(0, 1_000_000) for _ in range(20_000_000)]
print(get_k_th_largest(0, len(ARR)-1, 0))


