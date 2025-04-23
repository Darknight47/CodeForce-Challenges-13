"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1392/A ------------------------------------

Lord Omkar has permitted you to enter the Holy Church of Omkar! To test your worthiness, Omkar gives you a password which you must interpret!

A password is an array a of n positive integers. You apply the following operation to the array: pick any two adjacent numbers that are not equal to each other and replace them with their sum. 
Formally, choose an index i such that 1≤i<n and a(i) ≠ a(i+1), delete both a(i) and a(i)+1 from the array and put a(i)+a(i)+1 in their place.

For example, for array [7,4,3,7] you can choose i=2 and the array will become [7,4+3,7]=[7,7,7]. 
Note that in this array you can't apply this operation anymore.

Notice that one operation will decrease the size of the password by 1. 
What is the shortest possible length of the password after some number (possibly 0) of operations?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 2⋅10^5) — the length of the password.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the initial contents of your password.

The sum of n over all test cases will not exceed 2⋅10^5.

Output
For each password, print one integer: the shortest possible length of the password after some number of operations.

Input:
2
4
2 1 3 1
2
420 420

Output:
1
2
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set(arr)
    if(len(tempSet) == 1):
        print(sze)
    else:
        print(1)