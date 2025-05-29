"""

---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2000/A -----------------------------------

Dmitry wrote down t integers on the board, and that is good. He is sure that he lost an important integer n among them, and that is bad.

The integer n had the form 10^x (x ≥ 2), where the symbol '^' denotes exponentiation.. Something went wrong, and 
Dmitry missed the symbol '^' when writing the important integer. For example, instead of the integer 10^5, he would have written 10^5, and instead of 10^19, he would have written 10^19.

Dmitry wants to understand which of the integers on the board could have been the important integer and which could not.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 10^4) — the number of integers on the board.

The next t lines each contain an integer a (1 ≤ a ≤ 10000) — the next integer from the board.

Output
For each integer on the board, output "YES" if it could have been the important integer and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Input:
7
100
1010
101
105
2033
1019
1002

Output:
NO
YES
NO
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n = input()
    if(len(n) < 3):
        print("NO")
    else:
        sub = n[0] + n[1]
        temp = n[2]
        if(len(n) == 3 and sub == '10' and temp != '0' and temp != '1'):
            print("YES")
        elif(len(n) > 3 and sub == '10' and temp != '0'):
            print("YES")
        else:
            print("NO")