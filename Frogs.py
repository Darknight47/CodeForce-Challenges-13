"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2055/A ----------------------------------------------

There are n lilypads arranged in a row, numbered from 1 to n from left to right. Alice and Bob are frogs initially positioned on distinct lilypads, a and b, respectively. 
They take turns jumping, starting with Alice.

During a frog's turn, it can jump either one space to the left or one space to the right, as long as the destination lilypad exists. For example, on Alice's first turn, she can jump to either lilypad a−1
 or a+1, provided these lilypads are within bounds. It is important to note that each frog must jump during its turn and cannot remain on the same lilypad.

However, there are some restrictions:

The two frogs cannot occupy the same lilypad. This means that Alice cannot jump to a lilypad that Bob is currently occupying, and vice versa.
If a frog cannot make a valid jump on its turn, it loses the game. As a result, the other frog wins.
Determine whether Alice can guarantee a win, assuming that both players play optimally. It can be proven that the game will end after a finite number of moves if both players play optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first and only line of each test case contains three integers n, a, and b (2≤n≤100, 1≤a,b≤n, a≠b) — the number of lilypads, and the starting positions of Alice and Bob, respectively.

Note that there are no constraints on the sum of n over all test cases.

Output
For each test case, print a single line containing either "YES" or "NO", representing whether or not Alice has a winning strategy.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
5
2 1 2
3 3 1
4 2 3
5 2 4
7 6 2

Output:
NO
YES
NO
YES
YES
"""


cases = int(input())
for _ in range(cases):
    n, a, b = map(int, input().split())
    if((a % 2 == 0 and b % 2 == 0) or
       (a % 2 == 1 and b % 2 == 1)):
        print("YES")
    else:
        print("NO")