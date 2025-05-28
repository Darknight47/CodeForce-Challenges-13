"""

------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2071/A ---------------------------------------

Let's introduce a two-player game, table tennis, where a winner is always decided and draws are impossible.

Three players, Sosai, Fofo, and Hohai, want to spend the rest of their lives playing table tennis. They decided to play forever in the following way:

In each match, two players compete while the third spectates.

To ensure fairness, no player can play three times in a row. The player who plays twice in a row must sit out as a spectator in the next match, 
which will be played by the other two players. Otherwise, the winner and the spectator will play in the next match, while the loser will spectate.
Now, the players, fully immersed in this infinite loop of matches, have tasked you with solving the following problem:

Given an integer k, determine whether the spectator of the first match can be the spectator in the k-th match.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The only line of each test case contains one integer k (1 ≤ k ≤ 10^9).

Output
For each test case, print "YES" (without quotes) if the spectator of the first match can be the spectator of the k-th match, and "NO" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
4
1
2
333
1000000000

Output:
YES
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    print("YES" if n % 3 == 1 else "NO")