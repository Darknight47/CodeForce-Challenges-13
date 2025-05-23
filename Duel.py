"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2109/A -------------------------------------

Mouf arranged the n players in a line, numbered from 1 to n. They then held n−1 consecutive duels: for each i from 1 to n−1, player i faced player i+1, 
producing one winner and one loser per match. Afterward, each player reports a value ai(0 ≤ a(i) ≤ 1):

0 indicating they won no duels;1 indicating they won at least one duel.
Since some may lie about their results (e.g., reporting a 1 instead of a 0, or vice versa) to influence prize outcomes, 
Mouf will cancel the tournament if he can prove any report to be false.

Given the array a, determine whether at least one player must be lying.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains one integer n (2 ≤ n ≤ 100) — the number of players in the tournament.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 1) — denoting the report of the i-th player.

Output
For each test case, print "YES" (without quotes) if there is at least one liar among the players, and "NO" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
6
3
0 1 0
2
0 0
2
1 1
4
0 1 1 1
4
1 0 0 1
7
0 1 0 1 0 1 0

Output:
NO
YES
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    oneZero = False
    lier = False
    for i in range(sze - 1):
        first = arr[i]
        second = arr[i + 1]
        if(first == 0 and second == 0):
            lier = True
        elif((first == 0 and second == 1) or (first == 1 and second == 0)):
            oneZero = True
    if(lier or not oneZero):
        print("YES")
    elif(not lier and oneZero):
        print("NO")