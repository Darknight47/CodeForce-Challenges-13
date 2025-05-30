"""
----------------------------------- Link for the challenge: https://codeforces.com/contest/1671/problem/A -----------------------------------

You are given a string s. 
You have to determine whether it is possible to build the string s out of strings aa, aaa, bb and/or bbb by concatenating them. You can use the strings aa, aaa, bb and/or bbb any number of times and in any order.

For example:
aaaabbb can be built as aa + aa + bbb;
bbaaaaabbb can be built as bb + aaa + aa + bbb;
aaaaaa can be built as aa + aa + aa; abab cannot be built from aa, aaa, bb and/or bbb.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of one line containing the string s (1 ≤ |s| ≤ 50), consisting of characters a and/or b.

Output
For each test case, print YES if it is possible to build the string s. Otherwise, print NO.

You may print each letter in any case (for example, YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).

Input:
8
aaaabbb
bbaaaaabbb
aaaaaa
abab
a
b
aaaab
bbaaa

Output:
YES
YES
YES
NO
NO
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    s = input()
    ok = True
    for j in range(len(s)):
        left_condition = (j == 0 or s[j] != s[j - 1])
        right_condition = (j == len(s) - 1 or s[j] != s[j + 1])
        if left_condition and right_condition:
            ok = False
            break
    print("YES" if ok else "NO")