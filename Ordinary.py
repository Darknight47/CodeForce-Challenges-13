"""

--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1520/B ----------------------------------------

Let's call a positive integer n ordinary if in the decimal notation all its digits are the same. For example, 1, 2 and 99 are ordinary numbers, but 719 and 2021 are not ordinary numbers.

For a given number n, find the number of ordinary numbers among the numbers from 1 to n.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4). Then t test cases follow.

Each test case is characterized by one integer n (1 ≤ n ≤ 10^9).

Output
For each test case output the number of ordinary numbers among numbers from 1 to n.

Input:
6
1
2
3
4
5
100

Output:
1
2
3
4
5
18
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n < 10):
        print(n)
    else:
        length = len(str(n))
        first_digit = int(str(n)[0])
        # Counting ordinary numbers with fewer digits
        count = (length - 1) * 9
        # Building the smallest ordinary number with same length and first digit
        ordinary_same_length = int(str(first_digit) * length)
        # If it's less than or equal to n, we can include it
        if ordinary_same_length <= n:
            count += first_digit
        else:
            count += first_digit - 1
        print(count)
