"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2096/A -------------------------------

You are the proud owner of n sticks. Each stick has an integer length from 1 to n. The lengths of the sticks are distinct.

You want to arrange the sticks in a row. There is a string s of length n−1 that describes the requirements of the arrangement.

Specifically, for each i from 1 to n−1:

If s(i) = <, then the length of the stick at position i+1 must be smaller than all sticks before it;
If s(i) = >, then the length of the stick at position i+1 must be larger than all sticks before it.
Find any valid arrangement of sticks. We can show that an answer always exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the number of sticks.

The second line of each test case contains a single string s of length n−1 consisting of characters < and > — describing the requirements of the arrangement.

Output
For each test case, output n integers a1,a2,…,an (1 ≤ a(i) ≤ n, the a(i) are distinct) — the lengths of the sticks in order. 
If there are multiple solutions, print any of them.

Input:
5
2
<
5
<<><
2
>
3
<>
7
><>>><

Output:
2 1 
4 3 2 5 1 
1 2 
2 1 3 
3 4 2 5 6 7 1 
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = input()
    numbers = list(range(1, sze + 1))
    ans = []
    for i in range(len(arr) - 1, -1, -1):
        tempChar = arr[i]
        if(tempChar == '<'):
            tempNum = min(numbers)
        else:
            tempNum = max(numbers)
        numbers.remove(tempNum)
        ans.append(tempNum)
    if(len(numbers) >= 1):
        ans.append(numbers[0])
    print(*ans[::-1])