"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2075/A -----------------------------

You are given two integers n and k; k is an odd number not less than 3. Your task is to turn n into 0.

To do this, you can perform the following operation any number of times: choose a number x from 1 to k and subtract it from n. 
However, if the current value of n is even (divisible by 2), then x must also be even, and if the current value of n is odd (not divisible by 2), then x must be odd.

In different operations, you can choose the same values of x, but you don't have to. So, there are no limitations on using the same value of x.

Calculate the minimum number of operations required to turn n into 0.

Input
The first line contains one integer t (1 ≤ t ≤ 10000) — the number of test cases.

Each test case consists of one line containing two integers n and k (3 ≤ k ≤ n ≤ 10^9, k is odd).

Output
For each test case, output one integer — the minimum number of operations required to turn n into 0.

Input:
8
39 7
9 3
6 3
999967802 3
5 5
6 5
999999999 3
1000000000 3

Output:
7
4
3
499983901
1
2
499999999
500000000
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    ans = 0
    if(n % 2 == 1):
        n -= k
        ans = 1
    k -= 1
    ans += (n // k) + (1 if n % k != 0 else 0)
    print(ans)