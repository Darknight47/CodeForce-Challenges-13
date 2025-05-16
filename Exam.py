"""
-------------------------------- Link for the challenge: https://codeforces.com/contest/1999/problem/D -------------------------------------------------

Slavic has a very tough exam and needs your help in order to pass it. Here is the question he is struggling with:

There exists a string s, which consists of lowercase English letters and possibly zero or more "?".

Slavic is asked to change each "?" to a lowercase English letter such that string t becomes a subsequence (not necessarily continuous) of the string s.

Output any such string, or say that it is impossible in case no string that respects the conditions exists.

Input
The first line contains a single integer T (1 ≤ T ≤ 10^4) — the number of test cases.

The first line of each test case contains a single string s (1≤|s|≤2⋅10^5, and s consists only of lowercase English letters and "?"-s)  – the original string you have.

The second line of each test case contains a single string t (1≤|t|≤|s|, and t consists only of lowercase English letters)  – the string that should be a subsequence of string s.

The sum of |s| over all test cases doesn't exceed 2⋅10^5, where |x| denotes the length of the string x.

Output
For each test case, if no such string exists as described in the statement, output "NO" (without quotes).

Otherwise, output "YES" (without quotes). Then, output one line — the string that respects all conditions.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes", and "Yes" will be recognized as a positive response).

If multiple answers are possible, you can output any of them.

Input:
5
?????
xbx
ab??e
abcde
ayy?x
a
ab??e
dac
paiu
mom

Output:
YES
xabax
YES
abcde
YES
ayyyx
NO
NO
"""
cases = int(input())
for _ in range(cases):
    s = list(input())
    t = list(input())
    i = 0
    j = 0
    i = 0
    idx = 0
    while i < len(s):
        if(idx < len(t)):
            if s[i] == '?':
                s[i] = t[idx]
                idx += 1
            elif s[i] == t[idx]:
                idx += 1
        else:
            if s[i] == '?':
                s[i] = 'a'
        i += 1
    if(idx >= len(t)):
        print("YES")
        print("".join(s))
    else:
        print("NO")