"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2074/B --------------------------------

The pink soldiers have given you a sequence a consisting of n positive integers.

You must repeatedly perform the following operation until there is only 1 element left.

Choose two distinct indices i and j.
Then, choose a positive integer value x such that there exists a non-degenerate triangle ∗ with side lengths a(i), a(j), and x.
Finally, remove two elements a(i) and a(j), and append x to the end of a.
Please find the maximum possible value of the only last element in the sequence a.

∗ A triangle with side lengths a, b, c is non-degenerate when a+b > c, a+c > b, b+c > a.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 1000) — the elements of the sequence a.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output the maximum possible value of the only last element on a separate line.

Input:
4
1
10
3
998 244 353
5
1 2 3 4 5
9
9 9 8 2 4 4 3 5 3

Output:
10
1593
11
39
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    tempSum = 0
    for i in range(sze):
        if(tempSum == 0):
            tempSum = arr[0]
        else:
            temp = (tempSum + arr[i]) - 1
            tempSum = temp
            ans = tempSum
    print(ans if sze > 1 else tempSum)