"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1993/A ---------------------------------

Tim is doing a test consisting of 4n questions; each question has 4 options: 'A', 'B', 'C', and 'D'. 
For each option, there are exactly n correct answers corresponding to that option — 
meaning there are n questions with the answer 'A', n questions with the answer 'B', n questions with the answer 'C', and n questions with the answer 'D'.

For each question, Tim wrote his answer on the answer sheet. If he could not figure out the answer, he would leave a question mark '?' for that question.

You are given his answer sheet of 4n characters. What is the maximum number of correct answers Tim can get?

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 100).

The second line of each test case contains a string s of 4n characters (s(i) ∈ {A,B,C,D,?}) — Tim's answers for the questions.

Output
For each test case, print a single integer — the maximum score that Tim can achieve.

Input:
6
1
ABCD
2
AAAAAAAA
2
AAAABBBB
2
????????
3
ABCABCABCABC
5
ACADC??ACAC?DCAABC?C

Output:
4
2
4
0
9
13
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    parity_counts = Counter(s)
    ans = 0
    for tuple in parity_counts.items():
        tk = tuple[0]
        tv = tuple[1]
        if(tk != '?' and tv >= sze):
            ans += sze
        elif(tk != '?' and tv < sze):
            ans += tv
    print(ans)