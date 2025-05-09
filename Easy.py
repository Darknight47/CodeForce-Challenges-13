"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2044/A ------------------------------------

Cube is given an integer n. She wants to know how many ordered pairs of positive integers (a,b) there are such that a=n−b. Since Cube is not very good at math, please help her!

Input
The first line contains an integer t (1 ≤ t ≤ 99) — the number of test cases.

The only line of each test case contains an integer n (2 ≤ n ≤ 100).

Output
For each test case, output the number of ordered pairs (a,b)  on a new line.

Input:
3
2
4
6

Output:
1
3
5
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    print(n - 1)