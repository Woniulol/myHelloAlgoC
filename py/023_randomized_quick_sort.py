"""
Flags

[0, n-1], get an x (value, not index) in between, split the original arr to
two parts, left part <= x, right part > x and move x to the last element of left part.

so that we know x is sorted.

<= x, x, >x, the position on x is fixed.
"""
from random import random, randint

def quick_sort(l: int, r: int) -> None:
    global ARR

    if l >= r:
        return

    x: int = ARR[l + int(random() * (r - l + 1))]
    mid: int = partition(l, r, x)

    quick_sort(l=l, r=(mid - 1))
    quick_sort(l=(mid + 1), r=r)


def partition(l: int, r: int, x: int):

    l_cur = l
    a = l
    xi = 0
    while a <= r:
        if ARR[a] <= x:
            ARR[a], ARR[l_cur] = ARR[l_cur], ARR[a]
            if ARR[l_cur] == x:
                xi = l_cur
            l_cur += 1
            a += 1
        else:
            ARR[r], ARR[a] = ARR[a], ARR[r]
            r -= 1

    ARR[xi], ARR[l_cur - 1] = ARR[l_cur - 1], ARR[xi]
    return l_cur - 1

if __name__ == "__main__":
    # ARR = [2, 3, 5, 3, 5, 6, 3, 4]
    ARR = [randint(0,9) for _ in range(5000)]
    quick_sort(0, len(ARR)-1)
    print(ARR)
