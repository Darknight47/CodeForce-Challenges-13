"""
---------------------------------------- Link for the challenge: https://codeforces.com/contest/1351/problem/B ----------------------------------------

Vasya claims that he had a paper square. He cut it into two rectangular parts using one vertical or horizontal cut. 
Then Vasya informed you the dimensions of these two rectangular parts. You need to check whether Vasya originally had a square. 
In other words, check if it is possible to make a square using two given rectangles.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases in the input. Then t test cases follow.

Each test case is given in two lines.

The first line contains two integers a(1) and b(1) (1 ≤ a1, b1 ≤ 100) — the dimensions of the first one obtained after cutting rectangle. 
The sizes are given in random order (that is, it is not known which of the numbers is the width, and which of the numbers is the length).

The second line contains two integers a(2) and b(2) (1 ≤ a2, b2 ≤ 100) — the dimensions of the second obtained after cutting rectangle. 
The sizes are given in random order (that is, it is not known which of the numbers is the width, and which of the numbers is the length).

Output
Print t answers, each of which is a string "YES" (in the case of a positive answer) or "NO" (in the case of a negative answer). The letters in words can be printed in any case (upper or lower).

Input:
3
2 3
3 1
3 2
1 3
3 3
1 3

Output:
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ok = False
    minNum = min(a, b)
    minNum2 = min(c, d)
    maxNum = max(a, b)
    maxNum2 = max(c, d)
    temp = minNum + minNum2
    if(temp == maxNum == maxNum2):
        print("YES")
    else:
        print("NO")