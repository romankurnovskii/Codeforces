########################################### Libraries ####################################################

import bisect
import sys
import math
import os
import time
from queue import PriorityQueue
from io import BytesIO, IOBase
from collections import defaultdict, Counter
from bisect import bisect_right

########################################### Definitions ####################################################

INF = sys.maxsize
BUFSIZE = 4096

############################################# Inputs ######################################################


def inp():
    return sys.stdin.readline().rstrip("\r\n")  # read line as string


def inp_int():
    return int(inp())  # read input as integer. '1' -> 1


def inp_int_list():
    return list(map(int, inp().split()))


def inp_str_list():
    return list(inp())


############################################# Data Structures ######################################################


class SegmentTree:  # //O(logn) for operations and O(n) for building//
    def init(
        arr,
    ):  # n shld be a power of 2...hence add extra zeros before itself if needed //O(n)//
        n = len(arr)
        tree = [0] * (2 * n)
        for i in range(n):
            # The actual array is between indices n to 2*n-1 the first nodes store sums
            tree[n + i] = arr[i]

        for i in range(n - 1, -1, -1):
            # parent node value  = child node's sum i<<1 = 2*i, i<<1 |1 = 2*i+1
            tree[i] = tree[i << 1] + tree[(i << 1) | 1]
        return tree

    def add(
        tree, i, v
    ):  # Sets vertex i to value v (i shld be 0 based indexing) //O(logn)//
        # As the actual array is between n and 2*n-1, we add n to i (n = len(tree)//2)
        i += len(tree) // 2
        tree[i] = v
        while i > 1:
            tree[i >> 1] = tree[i] + tree[i ^ 1]
            i >>= 1
            # Calculating the values of prev nodes. (eg if node 9 is changed 9>>1 = 4 takes values of node i(9) and node i^1(8))

    # calculates the sum of values in the range [l,r-1] (l and r take 0 based indexing) //O(logn)//
    def range_sum(tree, l, r):
        l += len(tree) // 2
        r += len(tree) // 2
        sum = 0
        while l < r:
            if l & 1:
                # If the index is odd, add its value to sum. if the index is even it means there would be a parent
                sum += tree[l]
                l += 1  # of this with odd index
            if r & 1:
                r -= 1
                sum += tree[r]
            l >>= 1
            r >>= 1
        return sum


############################################# Solution ######################################################


def solve():
    s = inp()
    print()


def run():
    for _ in range(inp_int()):
        solve()


if __name__ == "__main__":
    CODE_DEBUG = 1
    if os.environ.get("CODE_DEBUG") or CODE_DEBUG:
        sys.stdin = open("./input.txt", "r")
        start_time = time.time()
        run()
        print("\n--- %s seconds ---\n" % (time.time() - start_time))
    else:
        run()
