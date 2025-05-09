"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1957/A --------------------------------

You are given n sticks of lengths a1,a2,…,an. Find the maximum number of regular (equal-sided) polygons you can construct simultaneously, such that:

Each side of a polygon is formed by exactly one stick.
No stick is used in more than 1 polygon.
Note: Sticks cannot be broken.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of sticks available.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100) — the stick lengths.

Output
For each test case, output a single integer on a new line — the maximum number of regular (equal-sided) polygons you can make simultaneously from the sticks available.

Input:
4
1
1
2
1 1
6
2 2 3 3 3 3
9
4 2 2 2 2 4 2 4 4

Output:
0
0
1
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set(arr)
    ans = 0
    for num in tempSet:
        temp = arr.count(num)
        ans += (temp // 3)
    print(ans)