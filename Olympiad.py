"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2091/A --------------------------------------

The final of the first Olympiad by IT Campus "NEIMARK" is scheduled for March 1, 2025. 
A nameless intern was tasked with forming the date of the Olympiad using digits — 01.03.2025.

To accomplish this, the intern took a large bag of digits and began drawing them one by one. 
In total, he drew n digits — the digit a(i) was drawn in the i-th turn.

You suspect that the intern did extra work. Determine at which step the intern could have first assembled the digits to form the date of the Olympiad 
(the separating dots can be ignored), or report that it is impossible to form this date from the drawn digits. Note that leading zeros must be displayed.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 20).

The second line of each test case contains n integers a(i) (0 ≤ a(i) ≤ 9) — the numbers that the intern pulled out in chronological order.

Output
For each test case, output the minimum number of digits that the intern could pull out. If all the digits cannot be used to make a date, output the number 0.

Input:
4
10
2 0 1 2 3 2 5 0 0 1
8
2 0 1 2 3 2 5 0
8
2 0 1 0 3 2 5 0
16
2 3 1 2 3 0 1 9 2 1 0 3 5 4 0 3

Output:
9
0
8
15
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    one = 1
    zeros = 3
    three = 1
    twos = 2
    five = 1
    ans = 0
    for num in arr:
        if(one <= 0 and zeros <= 0 and three <= 0 and twos <= 0 and five <= 0):
            break
        if(num == 1):
            one -= 1
        elif(num == 0):
            zeros -= 1
        elif(num == 3):
            three -= 1
        elif(num == 2):
            twos -= 1
        elif(num == 5):
            five -= 1
        ans += 1
    if(one > 0 or zeros > 0 or three > 0 or twos > 0 or five > 0):
        print(0)
    else:
        print(ans)