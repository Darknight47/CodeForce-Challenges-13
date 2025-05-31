"""
----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1883/B -------------------------

You are given a string s of length n, consisting of lowercase Latin letters, and an integer k.

You need to check if it is possible to remove exactly k characters from the string s in such a way that the remaining characters can be rearranged to form a palindrome. 
Note that you can reorder the remaining characters in any way.

A palindrome is a string that reads the same forwards and backwards. For example, the strings "z", "aaa", "aba", "abccba" are palindromes, while the strings "codeforces", "reality", "ab" are not.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of the test cases. This is followed by their description.

The first line of each test case contains two integers n and k (0 ≤ k < n ≤ 10^5) — the length of the string s and the number of characters to be deleted.

The second line of each test case contains a string s of length n, consisting of lowercase Latin letters.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "YES" if it is possible to remove exactly k characters from the string s in such a way that the remaining characters can be rearranged to form a palindrome, and "NO" otherwise.

You can output the answer in any case (uppercase or lowercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.

Input:
14
1 0
a
2 0
ab
2 1
ba
3 1
abb
3 2
abc
6 2
bacacd
6 2
fagbza
6 2
zwaafa
7 2
taagaak
14 3
ttrraakkttoorr
5 3
debdb
5 4
ecadc
5 3
debca
5 3
abaac

Output:
YES
NO
YES
YES
YES
YES
NO
NO
YES
YES
YES
YES
NO
YES
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    s = input()
    parity_counts = Counter(s)
    temp = 0
    for tuple in parity_counts.items():
        tv = tuple[1]
        if(tv % 2 == 1):
            temp += 1
    if(temp <= (k + 1)):
        print("YES")
    else:
        print("NO")