"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1946/A -------------------------------------------

You are given an array a of n integers.

The median of an array q1,q2,…,qk is the number p⌈k/2⌉, where p is the array q sorted in non-decreasing order. 
For example, the median of the array [9,5,1,2,6] is 5, as in the sorted array [1,2,5,6,9], the number at index ⌈5/2⌉ = 3 is 5, and the median of the array [9,2,8,3] is 3, as in the sorted array [2,3,8,9], 
the number at index ⌈4/2⌉ = 2 is 3.

You are allowed to choose an integer i (1 ≤ i ≤ n) and increase a(i) by 1 in one operation.

Your task is to find the minimum number of operations required to increase the median of the array.

Note that the array a may not necessarily contain distinct numbers.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the array a.

It is guaranteed that the sum of the values of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the minimum number of operations required to increase the median of the array.

Input:
8
3
2 2 8
4
7 3 3 1
1
1000000000
5
5 5 5 4 5
6
2 1 2 3 1 4
2
1 2
2
1 1
4
5 5 5 5

Output:
1
2
1
3
2
1
2
3
"""
import math
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    medIdx = math.ceil(sze / 2) - 1
    med = arr[medIdx]
    ans = 0
    for i in range(medIdx, sze):
        if(arr[i] <= med):
            ans += ((med + 1) - arr[i])
        else:
            break
    print(ans)