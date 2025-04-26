"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2092/A --------------------------------

Kamilka has a flock of n sheep, the i-th of which has a beauty level of a(i). All a(i) are distinct. 
Morning has come, which means they need to be fed. Kamilka can choose a non-negative integer d and give each sheep d bunches of grass. After that, the beauty level of each sheep increases by d.

In the evening, Kamilka must choose exactly two sheep and take them to the mountains. 
If the beauty levels of these two sheep are x and y (after they have been fed), then Kamilka's pleasure from the walk is equal to gcd(x,y), 
where gcd(x,y) denotes the greatest common divisor (GCD) of integers x and y.

The task is to find the maximum possible pleasure that Kamilka can get from the walk.

Input
Each test consists of several test cases. The first line contains one integer t (1 ≤ t ≤ 500), the number of test cases. The description of the test cases follows.

The first line of each test case contains one integer n (2 ≤ n ≤ 100), the number of sheep Kamilka has.

The second line of each test case contains n distinct integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the beauty levels of the sheep.

It is guaranteed that all a(i) are distinct.

Output
For each test case, output a single integer: the maximum possible pleasure that Kamilka can get from the walk.

Input:
4
2
1 3
5
5 4 3 2 1
3
5 6 7
3
1 11 10

Output:
2
4
2
10
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    diff = arr[sze - 1] - arr[0]
    print(diff)