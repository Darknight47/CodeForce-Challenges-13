"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2084/A -------------------------------------

You are given an integer n. Find any permutation p of length n∗ such that:

For all 2 ≤ i ≤ n, max(pi−1,pi) mod i†=i−1 is satisfied.
If it is impossible to find such a permutation p, output −1.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 99). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100).

Output
For each test case:

If such a permutation p doesn't exist, output a single integer −1.
Otherwise, output n integers p1,p2,…,pn — the permutation p you've found. If there are multiple answers, output any of them.

Input:
4
2
3
4
5

Output:
-1
3 2 1
-1
1 5 2 3 4
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n % 2 == 0):
        print(-1)
    else:
        print(n, end=" ")
        print(*range(1, n))