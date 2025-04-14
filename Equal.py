"""
----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2001/A -----------------------------------------

You are given a cyclic array a1,a2,…,an.

You can perform the following operation on a at most n−1 times:

Let m be the current size of a, you can choose any two adjacent elements where the previous one is no greater than the latter one 
(In particular, a(m) and a(1) are adjacent and am is the previous one), and delete exactly one of them. In other words, choose an integer i (1 ≤ i ≤ m) where ai≤a(i mod m)+1 holds, 
and delete exactly one of a(i) or a(i mod m)+1 from a.
Your goal is to find the minimum number of operations needed to make all elements in a equal.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ n) — the elements of array a.

Output
For each test case, output a single line containing an integer: the minimum number of operations needed to make all elements in a equal.

Input:
7
1
1
3
1 2 3
3
1 2 2
5
5 4 3 2 1
6
1 1 2 2 3 3
8
8 7 6 3 8 7 6 3
6
1 1 4 5 1 4

Output:
0
2
1
4
4
6
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set(arr)
    if(len(tempSet) == 1):
        print(0)
    elif(len(tempSet) == sze):
        print(sze - 1)
    else:
        biggest = 0
        for num in tempSet:
            temp = arr.count(num)
            if(temp > biggest):
                biggest = temp
        print(sze - biggest)