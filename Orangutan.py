"""
----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2030/A -----------------------------------------

While exploring the jungle, you have bumped into a rare orangutan with a bow tie! You shake hands with the orangutan and offer him some food and water. In return...

The orangutan has gifted you an array a of length n. 
Using a, you will construct two arrays b and c, both containing n elements, in the following manner:

b(i) = min(a1,a2,…,ai) for each 1 ≤ i ≤ n.
c(i) = max(a1,a2,…,ai) for each 1 ≤ i ≤ n.

Define the score of (a) as ∑n(i=1) c(i) − b(i) (i.e. the sum of c(i)−b(i) over all 1 ≤ i ≤ n). Before you calculate the score, you can shuffle the elements of a however you want.

Find the maximum score that you can get if you shuffle the elements of a optimally.

Input
The first line contains t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 1000) — the number of elements in a.

The following line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 1000) — the elements of the array a.

It is guaranteed that the sum of n over all test cases does not exceed 1000.

Output
For each test case, output the maximum score that you can get.

Input:
3
1
69
3
7 6 5
5
1 1 1 2 2

Output:
0
4
4
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    tempMin = min(arr)
    tempMax = max(arr)
    ans = 0
    for i in range(n - 1):
        ans += tempMax - tempMin
    print(ans)