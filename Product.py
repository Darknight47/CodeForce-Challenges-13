"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1917/A -----------------------------------------

You are given an array of integers a1,a2,…,an. You can perform the following operation any number of times (possibly zero):

Choose any element a(i) from the array and change its value to any integer between 0 and a(i) (inclusive). 
More formally, if a(i) < 0, replace a(i) with any integer in [a(i),0], otherwise replace a(i) with any integer in [0,a(i)].
Let r be the minimum possible product of all the a(i) after performing the operation any number of times.

Find the minimum number of operations required to make the product equal to r. 
Also, print one such shortest sequence of operations. If there are multiple answers, you can print any of them.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) - the number of test cases. This is followed by their description.

The first line of each test case contains the a single integer n (1 ≤ n ≤ 100) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (−10^9 ≤ a(i) ≤ 10^9).

Output
For each test case:

The first line must contain the minimum number of operations k (0 ≤ k ≤ n).
The j-th of the next k lines must contain two integers i and x, which represent the j-th operation. That operation consists in replacing a(i) with x.

Input:
4
1
155
4
2 8 -1 3
4
-1 0 -2 -5
4
-15 -75 -25 -30

Output:
1
1 0
0
0
1
3 0
"""
import math
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    prod = math.prod(arr)
    if(prod > 0):
        print(1)
        print(1, 0)
    else:
        print(0)