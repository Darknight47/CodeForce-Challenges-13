"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1525/A ----------------------------------

You have an initially empty cauldron, and you want to brew a potion in it. The potion consists of two ingredients: magic essence and water. 
The potion you want to brew should contain exactly k% magic essence and (100−k)% water.

In one step, you can pour either one liter of magic essence or one liter of water into the cauldron. What is the minimum number of steps to brew a potion? You don't care about the total volume of the potion, only about the ratio between magic essence and water in it.

A small reminder: if you pour e liters of essence and w liters of water (e+w > 0) into the cauldron, then it contains (e/e+w) * 100% (without rounding) magic essence and (w/e+w) * 100% water.

Input
The first line contains the single t (1 ≤ t ≤ 100) — the number of test cases.

The first and only line of each test case contains a single integer k (1 ≤ k ≤ 100) — the percentage of essence in a good potion.

Output
For each test case, print the minimum number of steps to brew a good potion. It can be proved that it's always possible to achieve it in a finite number of steps.

Input:
3
3
100
25

Output:
100
1
4
"""
import math
cases = int(input())
for _ in range(cases):
    k = int(input())
    # v = 100 / gcd(k, 100)
    gcd = math.gcd(k, 100)
    liter = 100 // gcd
    print(liter)