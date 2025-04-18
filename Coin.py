"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2043/A -----------------------------------

Initially, you have a coin with value n. You can perform the following operation any number of times (possibly zero):

transform one coin with value x, where x is greater than 3 (x > 3), into two coins with value ⌊x4⌋.

What is the maximum number of coins you can have after performing this operation any number of times?

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of one line containing one integer n (1 ≤ n ≤ 10^18).

Output
For each test case, print one integer — the maximum number of coins you can have after performing the operation any number of times.

Input:
4
1
5
16
1000000000000000000

Output:
1
2
4
536870912
"""
cases = int(input())
for i in range(cases):
    n = int(input())
    ans = 1
    while n > 3:
        n //= 4
        ans *= 2
    print(ans)
