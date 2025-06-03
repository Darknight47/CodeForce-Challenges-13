"""
--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1433/B ------------------------------------------------

There is a bookshelf which can fit n books. The i-th position of bookshelf is a(i) = 1 if there is a book on this position and a(i) = 0 otherwise. It is guaranteed that there is at least one book on the bookshelf.

In one move, you can choose some contiguous segment [l;r] consisting of books (i.e. for each i from l to r the condition a(i) = 1 holds) and:

Shift it to the right by 1: move the book at index i to i+1 for all l ≤ i ≤ r. 
This move can be done only if r+1 ≤ n and there is no book at the position r+1.
Shift it to the left by 1: move the book at index i to i−1 for all l ≤ i ≤ r. 
This move can be done only if l−1≥1 and there is no book at the position l−1.
Your task is to find the minimum number of moves required to collect all the books on the shelf as a contiguous (consecutive) segment (i.e. the segment without any gaps).

For example, for a=[0,0,1,0,1] there is a gap between books (a(4)=0 when a(3)=1 and a(5)=1), for a=[1,1,0] there are no gaps between books and for a=[0,0,0] there are also no gaps between books.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 200) — the number of test cases. Then t test cases follow.

The first line of the test case contains one integer n (1 ≤ n ≤ 50) — the number of places on a bookshelf. 
The second line of the test case contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 1), where a(i) is 1 if there is a book at this position and 0 otherwise. 
It is guaranteed that there is at least one book on the bookshelf.

Output
For each test case, print one integer: the minimum number of moves required to collect all the books on the shelf as a contiguous (consecutive) segment (i.e. the segment without gaps).

Input:
5
7
0 0 1 0 1 0 1
3
1 0 0
5
1 1 0 0 1
6
1 0 0 0 0 1
5
1 1 0 1 1

Output:
2
0
2
4
1
"""
import re
cases = int(input())
for _ in range(cases):
    sze = int(input())
    bin_str = input()
    bin_str = bin_str.replace(" ", "")
    matches = re.findall(r'(?<=1)(0+)(?=1)', bin_str)
    ans = sum(len(match) for match in matches)
    print(ans)